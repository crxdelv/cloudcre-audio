from http.server import BaseHTTPRequestHandler
import traceback, requests

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    try:
      req = requests.get('https:/' + self.path, stream=True)
      req.raise_for_status()
      self.send_header('Content-Type', 'audio/mp4')
      self.send_header('Access-Control-Allow-Origin', '*')
      self.send_header('Content-Disposition', 'attachment')
      self.send_response(200)
      for chunk in req.iter_content(chunk_size=8192):
        self.wfile.write(chunk)
    except:
      self.send_header('Content-Type', 'text/plain')
      self.send_header('Access-Control-Allow-Origin', '*')
      self.send_response(500)
      self.end_headers()
      self.wfile.write(traceback.format_exc.encode('utf-8'))