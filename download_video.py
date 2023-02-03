
import os
import subprocess
import cv2


def download_video(url, video_format):
    # Download the video using youtube-dl
    
    try:
        subprocess.check_call(["youtube-dl", "-f",  video_format, "--no-playlist", "--restrict-filenames", "--output",  "video/%(title)s.mp4", url])
        print("Video downloaded.")
    except subprocess.CalledProcessError as e:
        print("Error in downloading video:", e)
        exit()
    
    # Get the name of the video file
    video_file = os.path.basename(subprocess.check_output(["youtube-dl", "-f", "bestvideo+bestaudio", "--no-playlist", "--restrict-filenames", "--get-filename", url]).decode().strip())
    # print(video_file)
    video_name, _ = os.path.splitext(os.path.basename(video_file))
    video_name = video_name.split("-")[0]
    # video_name = video_name+".mp4.webm"  
    print(video_name,_)
    return video_name,_
