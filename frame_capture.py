import os
import subprocess
import cv2
def extract_frames(video_name):
    print(video_name)
    # if ".webm" in video_name:
    new_filename = video_name.replace(".webm", "")
    # vid = cv2.VideoCapture("video/"+new_filename)
    # else:    
    vid = cv2.VideoCapture("video/"+new_filename)
    
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