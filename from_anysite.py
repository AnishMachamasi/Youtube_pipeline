import os
import subprocess
import cv2

# Prompt the user to enter the URL of the YouTube video
url = input("Enter the URL of the YouTube video: ")
video_format = input("Enter the desired video format (e.g. mp4, best, worst, webm): ")
audio_format = input("Enter the desired audio format (e.g. mp3): ")

def download_video(url, video_format):
    # Download the video using youtube-dl
    
    try:
        subprocess.check_call(["youtube-dl", "-f",  "bestvideo+bestaudio", "--no-playlist", "--restrict-filenames", "--output",  "video/%(title)s.mp4", url])
        print("Video downloaded.")
    except subprocess.CalledProcessError as e:
        print("Error in downloading video:", e)
        exit()
    
    # Get the name of the video file
    video_file = os.path.basename(subprocess.check_output(["youtube-dl", "-f", "bestvideo+bestaudio", "--no-playlist", "--restrict-filenames", "--get-filename", url]).decode().strip())
    print(video_file)
    video_name, _ = os.path.splitext(os.path.basename(video_file))
    video_name = video_name.split("-")[0]
    video_name = video_name+".mp4.webm"  
    print(video_name)
    return video_name

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
    print(audio_name)

# def extract_frames(video_name):
#     # Extract the frames using OpenCV
#     # Open the video using OpenCV
#     video = cv2.VideoCapture("video/"+video_name)

#     # Get the video frame count
#     frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
#     print(frame_count)

#     # Get the video name
#     video_name = url.split("/")[-1]

#     # Create a directory to store the frames
#     os.makedirs("frames/"+video_name, exist_ok=True)

#     # Extract the frames
#     for i in range(frame_count):
#         success, frame = video.read()
#         if success:
#             cv2.imwrite("frames/"+video_name+"/frame"+str(i)+".jpg", frame)
#         if i % 50 == 0:
#             print(f"Processed {i} frames.")
#     print("Frames extracted.")
    
#     # Release the video
#     video.release()



def extract_frames(video_name):
    # Extract the frames using OpenCV
    # Open the video using OpenCV
    video = cv2.VideoCapture("video/"+video_name)

    # Get the video frame count
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print(frame_count)

    # # Get the video name
    # video_name = url.split("/")[-1]

    # Create a directory to store the frames
    os.makedirs("frames/"+video_name, exist_ok=True)
    
    # Ask the user whether they want to resize the frames
    resize_frames = input("Do you want to resize the frames? (yes/no): ")
    frame_width = 0
    frame_height = 0
    
    # If the user wants to resize the frames, ask for the desired size
    if resize_frames == "yes":
        frame_width = int(input("Enter the desired width of the frames: "))
        frame_height = int(input("Enter the desired height of the frames: "))
    
    # Extract the frames
    for i in range(frame_count):
        success, frame = video.read()
        if success:
            # Resize the frame if necessary
            if resize_frames == "yes":
                frame = cv2.resize(frame, (frame_width, frame_height))
            cv2.imwrite("frames/"+video_name+"/frame"+str(i)+".jpg", frame)
        if i % 50 == 0:
            print(f"Processed {i} frames.")
    print("Frames extracted.")
    
    # Release the video
    video.release()
    

video_name = download_video(url, video_format)
def monitor_pipeline(url, video_name):
    video_file = url.split("/")[-1] + ".mp4"
    if not os.path.exists("video/" + video_name):
        print("Download failed for video:", url)

monitor_pipeline(url, video_name)

download_audio(url, audio_format)
extract_frames(video_name)




