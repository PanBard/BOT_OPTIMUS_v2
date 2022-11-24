from distutils.debug import DEBUG
import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from detektor import Detektor, Kierownik
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
    going = vision.get_click_points(wykrywanie_obiektu.rectangles)
    bot.update_targets(going)
    bot.update_mapsony(going)
    bot.update_ikona_mapy(going)



    if BotState.MAPA == 1:
        Kierownik.SKRZYNKI = 0
        Kierownik.MAPA = 1
        Kierownik.POPRAWKA_MAPY = 0
        mapsony = vision.get_click_points(wykrywanie_obiektu.rectangles)
        bot.update_mapsony(mapsony)
        print("MAPA")

    if BotState.POPRAWKA_MAPY == 1:
        Kierownik.SKRZYNKI = 0
        Kierownik.MAPA = 0
        Kierownik.POPRAWKA_MAPY = 1
        ikona = vision.get_click_points(wykrywanie_obiektu.rectangles)
        bot.update_ikona_mapy(ikona)
        print("POPRAWKA_MAPY")

    if BotState.SKRZYNKI == 1:
        Kierownik.SKRZYNKI = 1
        Kierownik.MAPA = 0
        Kierownik.POPRAWKA_MAPY = 0
        targets = vision.get_click_points(wykrywanie_obiektu.rectangles)
        bot.update_targets(targets)
        print("SKRZYNKI")

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
