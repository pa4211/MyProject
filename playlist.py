from pytubefix import Playlist
import csv
import pandas as pd

# Define the playlist URL
URL = "https://youtube.com/playlist?list=PLSnP4pDlymf_WawWLJ61FncBf-V3IFY_o"

# Create a Playlist object
playlist = Playlist(URL)

# Extract video URLs (each URL must be in a list)
video_url_list = [[video.title, video.watch_url] for video in playlist.videos]  # ✅ FIXED

# Create a DataFrame (Optional)
#df = pd.DataFrame(video_url_list, columns=['URL'])

# Save to CSV
csv_filename = 'playlist.csv'
with open(csv_filename, 'w', newline="", encoding="utf-8") as file:
    csvwriter = csv.writer(file)  # Create a CSV writer object
    csvwriter.writerow(["URL", "Title"])  # Write header
    csvwriter.writerows(video_url_list)  # ✅ FIXED

# Print DataFrame
#print(df)
