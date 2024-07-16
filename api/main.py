from http.server import BaseHTTPRequestHandler
from functools import reduce
from pytubefix import YouTube
import traceback

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    dispose = 'dispose' in self.path
    try:
      yt = YouTube(self.path)
      streams = yt.streams.filter(only_audio=True)
      stream = reduce(lambda cur, obj: obj if cur.bitrate > obj.bitrate else cur, streams)
      stream.download('tmp', 'output', mp3=True)
      self.send_response(200)
      self.send_header('Content-Type', 'audio/mp4')
      self.send_header('Access-Control-Allow-Origin', '*')
      self.send_header('Content-Disposition', 'attachment')
      with open('/tmp/output.mp3', 'rb') as f:
        self.wfile.write(f.read())
    except:
      self.send_response(500)
      self.send_header('Content-Type', 'text/plain')
      self.send_header('Access-Control-Allow-Origin', '*')
      self.end_headers()
      self.wfile.write(traceback.format_exc().encode('utf-8'))
