
from pytubefix import YouTube
from pytubefix.cli import on_progress
url = "https://www.youtube.com/watch?v=MkB4JKgQYN0&list=PLQhgaMnae5AlZuKNIIzbKe2OZeXUMToU5&index=1"  
yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_audio_only()
ys.download()