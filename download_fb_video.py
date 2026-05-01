import yt_dlp
from yt_dlp.utils import download_range_func

#replace with folder location where you want to save the video
save_file = "/content/drive/MyDrive/output"

yt_opts = {
    "verbose": True,
    "outtmpl": save_file,
}

with yt_dlp.YoutubeDL(yt_opts) as ydl:
    ydl.download("https://www.facebook.com/reel/1499383088365257")
