import cv2
import os
vidcap = cv2.VideoCapture('video3.mp4')
success,image = vidcap.read()
count = 0
path = '/home/oz/Desktop/image-classification-keras/frames'
while success:
    if count >= 10:
        count = 0
        os.system('python test_network-only-fire.py -m firev10.model -i frames/frame0.jpg')
    
   # cv2.imwrite("frame%d.jpg" % count, image)          
    cv2.imwrite(os.path.join(path , "frame%d.jpg" % count), image)
    success,image = vidcap.read()
    print('Read a new frame: %d' % count , success)
    count += 1
