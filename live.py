import time
import urllib.request

url = input("Enter the streaming online video URL: ")
print("Recording video...")
response = urllib.request.urlopen(url)
filename = time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".avi"
f = open(filename, 'wb')

video_file_size_start = 0
video_file_size_end = 1048576 * 7  # end in 7 MB
block_size = 1024

while True:
    try:
        buffer = response.read(block_size)
        if not buffer:
            break
        video_file_size_start += len(buffer)
        if video_file_size_start > video_file_size_end:
            break
        f.write(buffer)

    except Exception as e:
        print("Error:", e)
f.close()
