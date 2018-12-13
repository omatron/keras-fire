from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2
import pyglet

ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained model model")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
orig = image.copy()

image = cv2.resize(image, (28, 28))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

print("[INFO] loading network...")
model = load_model(args["model"])

(notFire, fire) = model.predict(image)[0]

label2 ="Fire: {:.2f}%".format(fire*100)
print("Fire: {:.2f}%".format(fire*100))
print("Fire: {}".format(fire))
output = imutils.resize(orig, width=400)
if fire > 0.2:
    print("Alarme!!!")
    cv2.putText(output, label2, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 0, 255), 2)
else:
    cv2.putText(output, label2, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 255, 0), 2)
#cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,0.7, (100, 255, 0), 2)

cv2.imshow("Output", output)
if fire > 0.2:
    music = pyglet.media.load('alarm.wav')
    music.play()
    def exiter(dt):
        pyglet.app.exit()

    pyglet.clock.schedule_once(exiter, music.duration)
    pyglet.app.run()
    cv2.waitKey(0)
    exit(1)

else:
    cv2.waitKey(1000)
    exit(0)
