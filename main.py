from distutils.debug import DEBUG
import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from detektor import Detektor
from vision import Vision
from bot import BotState, Optimus_Logika



DEBUG = True

# initialize class1
wincap = WindowCapture('Dark Orbit')
wykrywanie_obiektu = Detektor()
vision = Vision()
bot = Optimus_Logika((wincap.offset_x, wincap.offset_y), (wincap.w, wincap.h))


wincap.start()
wykrywanie_obiektu.start()
bot.start()


loop_time = time()
while True:

    # get an updated image of the game
    if wincap.screenshot is None:
        continue
    
    wykrywanie_obiektu.update(wincap.screenshot)
    targets = vision.get_click_points(wykrywanie_obiektu.rectangles)
    bot.update_targets(targets)

    if DEBUG:
        # # draw the detec111tion results onto the original image
        detection_image = vision.draw_rectangles(wincap.screenshot, wykrywanie_obiektu.rectangles)
        # # display the images11
        cv.imshow('Matches', detection_image)
        pass
    key = cv.waitKey(1)
    if key == ord('q'):
        wincap.stop()
        wykrywanie_obiektu.stop()
        bot.stop()
        cv.destroyAllWindows()
        break

print('Done.')
