import os
import subprocess
import cv2
def download_audio(url, audio_format):
    # Extract the audio using ffmpeg
    print("Downloading audio...")
    try:
        subprocess.check_call(["youtube-dl", "-f", "bestaudio", "--extract-audio", "--audio-format", audio_format, "--output", "audio/%(title)s.mp4", url])
        print("Audio downloaded.")
    except subprocess.CalledProcessError as e:
        print("Error in downloading audio:", e)
        exit()


    # Get the name of the audio file
    audio_file = subprocess.check_output(["youtube-dl", "-f", "bestaudio", "--extract-audio", "--audio-format", audio_format, "--get-filename", url]).decode().strip()
    audio_name, _ = os.path.splitext(os.path.basename(audio_file))
    audio_name = audio_name.split("-")[0]
    audio_name = audio_name + ".mp3"