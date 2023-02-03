import os
import subprocess
import cv2
from download_video import download_video
from download_audio import download_audio
from frame_capture import extract_frames
url = input("Enter the URL of the YouTube video: ")
video_format = input("Enter the desired video format (e.g. mp4, best, worst, webm): ")
audio_format = input("Enter the desired audio format (e.g. mp3): ")


video_name = download_video(url, video_format)

def monitor_pipeline(url, video_name):
    video_file = url.split("/")[-1] + ".mp4"
    if not os.path.exists("video/" + video_name):
        print("Download failed for video:", url)

monitor_pipeline(url, video_name)

download_audio(url, audio_format)
print(video_name)
extract_frames(video_name)




