import json
import re
import urllib.request

from pytube import YouTube

# https://youtu.be/Ka77djMkSwg?si=Y16nry0RtgJYW0qy
api_key='AIzaSyCLGnVKxnU0GYR724XjPUhhJsReEYfXLNQ'
video_id='G3e-cpL7ofc'
url=f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"

json_url = urllib.request.urlopen(url) 
data = json.loads(json_url.read())
print(data)
