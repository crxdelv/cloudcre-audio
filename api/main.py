from pytubefix import YouTube
from http.server import BaseHTTPRequestHandler
import traceback

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    if len(self.path) < 2:
      return self.end('400 Bad Request: Incomplete Parameter', 400)
    path = None
    try:
      path = self.path.split("/")[1]
    except:
      return self.end('400 Bad Request: Invalid Parameter', 400)
    try:
      video = YouTube('https://youtu.be/' + path)
      stream = video.streams.filter(only_audio=True).first()
      stream.download(filename='output.mp3', output_path='/tmp/')
      self.send_response(200)
      self.send_header('Content-type', 'audio/mp3')
      self.send_header('Access-Control-Allow-Origin', '*')
      self.end_headers()
      with open('/tmp/output.mp3', 'rb') as f:
        self.wfile.write(f.read())
        return f.close()
    except Exception as e:
      if('regex_search' in str(e)):
        return self.end('400 Bad Request: Invalid Parameter', 400)
      if('unavailable' in str(e)):
        return self.end('404 Not Found: Unavailable', 404)
      traceback.print_exc()
  def end(self, text, status):
    self.send_response(status)
    self.send_header('Content-type', 'text/plain')
    self.send_header('Access-Control-Allow-Origin', '*')
    self.end_headers()
    self.wfile.write(text.encode('utf-8'))