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
    # print(video_name)
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
    # print(audio_name)

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
    if ".webm" in video_name:
        new_filename = video_name.replace(".webm", "")
        vid = cv2.VideoCapture("video/"+new_filename)
    else:    
        vid = cv2.VideoCapture("video/"+video_name)
    
    try:

        # creating a folder named data
        if not os.path.exists('data'):
            os.makedirs('data')

    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')  
    currentframe = 0
    count=0
    while (True):

        # reading from frame
        success, frame = vid.read()

        if success:
            if count%20==0:
                # continue creating images until video remains
                name = './data/frame' + str(currentframe) + '.jpg'
                print('Creating...' + name)

                # writing the extracted images
                cv2.imwrite(name, frame)

                # increasing counter so that it will
                # show how many frames are created
                currentframe += 1
            count+=1
        else:
            break
    vid.release()
    cv2.destroyAllWindows()


video_name = download_video(url, video_format)

def monitor_pipeline(url, video_name):
    video_file = url.split("/")[-1] + ".mp4"
    if not os.path.exists("video/" + video_name):
        print("Download failed for video:", url)

monitor_pipeline(url, video_name)

download_audio(url, audio_format)
print(video_name)
extract_frames(video_name)




