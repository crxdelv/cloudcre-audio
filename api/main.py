from pytubefix import YouTube
from pytube. innertube import _default_clients
from http.server import BaseHTTPRequestHandler
import traceback

_default_clients[ "ANDROID"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["ANDROID_EMBED"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS_EMBED"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS_MUSIC"]["context"]["client"]["clientVersion"] = "6.41"
_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    dispose = 'dispose' in self.path
    stream = None
    try:
      video = YouTube(self.path)
      stream = video.streams.filter(only_audio=True).first()
      stream.download(filename='output.mp3', output_path='/tmp/')
      self.send_response(200)
      self.send_header('Content-type', 'audio/mp3')
      if dispose:
        self.send_header('Content-disposition', 'attachment')
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
      return self.end(traceback.format_exc())
  def end(self, text, status):
    self.send_response(status)
    self.send_header('Content-type', 'text/plain')
    self.send_header('Access-Control-Allow-Origin', '*')
    self.end_headers()
    self.wfile.write(text.encode('utf-8'))