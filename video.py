
from pytube import Playlist
from pytube import YouTube
import csv

pl = Playlist("https://www.youtube.com/watch?v=isoLnspA-1E&list=PLqEJ_rxb3Xf0dTy_-dSqINnAD5tbmpUx8")
urls = pl.video_urls

for url in urls:
    vid_title = YouTube(url).title 