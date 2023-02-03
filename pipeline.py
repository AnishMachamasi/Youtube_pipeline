import pafy
import cv2
import subprocess

def download_video_and_audio(video_url):
    # Collect video data using pafy
    video = pafy.new(video_url)
    best_video = video.getbest(preftype="mp4")
    
    # Use ffmpeg to extract audio from the video file
    audio_file = video.title + ".mp3"
    subprocess.run(["ffmpeg", "-i", best_video.url, "-q:a", "0", audio_file])
    
    # Use opencv-python to extract frames from the video
    cap = cv2.VideoCapture(best_video.url)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Create a separate folder for each video
    video_folder = video.title
    subprocess.run(["mkdir", video_folder])
    
    for i in range(frame_count):
        ret, frame = cap.read()
        if ret:
            cv2.imwrite("{}/frame_{}.jpg".format(video_folder, i), frame)
    
    cap.release()

# Read multiple video URLs from the user
video_urls = []
while True:
    video_url = input("Enter a video URL (press Enter to finish): ")
    if video_url == "":
        break
    video_urls.append(video_url)

# Download video, audio, and frames for each URL
for video_url in video_urls:
    download_video_and_audio(video_url)
