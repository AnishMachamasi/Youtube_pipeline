from __future__ import unicode_literals
import youtube_dl
import subprocess
import os
import cv2

def download_video(url, directory):
    with youtube_dl.YoutubeDL() as ydl:
        result = ydl.extract_info(url, download=False)
        video_title = result.get('title', '').translate(str.maketrans(' ', '_'))
        video_ext = result.get('ext', '')
        ydl_opts = {
            'outtmpl': directory + '/{}.{}'.format(video_title, video_ext)
        }
        ydl = youtube_dl.YoutubeDL(ydl_opts)
        ydl.download([url])
        return '{}.{}'.format(video_title, video_ext)

def extract_audio(input_file, output_file):
    command = f'ffmpeg -i {input_file} -vn -ab 128k -ar 44100 -y {output_file}'
    subprocess.run(command, shell=True, check=True)
    
def extract_frames(video_file):
    # Extract the frames using OpenCV
    # Open the video using OpenCV
    video = cv2.VideoCapture("H:/code_rush_apprenticeship/task03-group_project/task1/video/"+video_file)

    # Get the video frame count
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print(frame_count)

    # # Get the video name
    # video_name = url.split("/")[-1]

    # Create a directory to store the frames
    os.makedirs("frames/"+video_file, exist_ok=True)
    
    # Ask the user whether they want to download all the frames or only some of them
    download_all = input("Do you want to download all the frames? (yes/no): ")

    # If the user wants to download only some of the frames, ask for the number of frames they want to download
    if download_all == "no":
        num_frames = int(input("Enter the number of frames you want to download: "))
    else:
        num_frames = frame_count
    
    # Ask the user whether they want to resize the frames
    resize_frames = input("Do you want to resize the frames? (yes/no): ")
    frame_width = 0
    frame_height = 0
    
    # If the user wants to resize the frames, ask for the desired size
    if resize_frames == "yes":
        frame_width = int(input("Enter the desired width of the frames: "))
        frame_height = int(input("Enter the desired height of the frames: "))
    
    # Extract the frames
    for i in range(num_frames):
        success, frame = video.read()
        if success:
            # Resize the frame if necessary
            if resize_frames == "yes":
                frame = cv2.resize(frame, (frame_width, frame_height))
            cv2.imwrite("frames/"+video_file+"/frame"+str(i)+".jpg", frame)
        if i % 50 == 0:
            print(f"Processed {i} frames.")
    print("Frames extracted.")
    
    # Release the video
    video.release()

video_folder = 'video/'
audio_folder = 'audio/'

valid_extensions = ['.webm', '.mp4']

urls = []
url = input("Enter a YouTube URL (or type 'done' when finished): ")

while url.lower() != 'done':
    urls.append(url)
    url = input("Enter another YouTube URL (or type 'done' when finished): ")

for url in urls:
    video_file = download_video(url, video_folder)
    print(video_file)
    extension = os.path.splitext(video_file)[1]
    
    if extension in valid_extensions:
        input_file = os.path.join(video_folder, video_file)
        output_file = os.path.join(audio_folder, os.path.splitext(video_file)[0] + ".mp3")
        extract_audio(input_file, output_file)
        
    extract_frames(video_file)
        

