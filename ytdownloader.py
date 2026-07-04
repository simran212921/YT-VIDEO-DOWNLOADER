import os
from yt_dlp import YoutubeDL

# Create downloads folder if it doesn't exist
if not os.path.exists("downloads"):
    os.makedirs("downloads")

print("=" * 40)
print("   YouTube Video Downloader")
print("=" * 40)

url = input("Enter YouTube Video URL: ")

options = {
    "outtmpl": "downloads/%(title)s.%(ext)s",
}

try:
    with YoutubeDL(options) as ydl:
        ydl.download([url])

    print("\nDownload completed!")
    print("Video saved in 'downloads' folder.")

except Exception as e:
    print("\nError:", e)
    
