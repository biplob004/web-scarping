!pip install youtube_dl

from __future__ import unicode_literals
import youtube_dl

video_links = ["https://www.youtube.com/watch?v=2S1dgHpqCdk&list=PLhhyoLH6IjfxeoooqP9rhU3HJIAVAJ3Vz"] # playlist link here

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
  ydl.download(video_links)
