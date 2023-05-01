import cv2
print(cv2.__version__)

videoFile='video.mp4'

cam = cv2.VideoCapture(videoFile)
currentFrame = 0
while(True):
    ret, frame = cam.read()
    if ret:
        cv2.imwrite(str(currentFrame) + '.jpg', frame)
        currentFrame += 1
    else:
        break
cam.release()
