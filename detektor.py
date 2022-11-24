import cv2 as cv
import numpy as np
from threading import Thread, Lock
from pomocnikDetektora import Pomocnik


class Kierownik:
    SKRZYNKI = 0
    MAPA = 0
    POPRAWKA_MAPY = 0

class Detektor:
    # threading properties
    stopped = True
    lock = None
    rectangles = []
    # properties
    cascade = None
    screenshot = None
    cel = "img/lo.jpg"
    moc_wykrywania = 0.7

    def __init__(self):
        # create a thread lock object
        self.lock = Lock()
        
        # load the trained model    

    def update(self, screenshot):
        self.lock.acquire()
        self.screenshot = screenshot
        self.lock.release()

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def run(self):
        # TODO: you can write your own time/iterations calculation to determine how fast this is
        while not self.stopped:
            if not self.screenshot is None:

                if Kierownik.SKRZYNKI == 1:
                    self.cel = "img/lo.jpg"
                    self.moc_wykrywania = 0.7

                if Kierownik.MAPA == 1:
                    self.cel = "img/mapa.jpg"
                    self.moc_wykrywania = 0.7

                if Kierownik.POPRAWKA_MAPY == 1:
                    self.cel = "img/poprawkaMapy.jpg"
                    self.moc_wykrywania = 0.9
                if Kierownik.SKRZYNKI == 1 or Kierownik.MAPA == 1 or Kierownik.POPRAWKA_MAPY == 1:
                    # do object detection
                    rectangles = self.rectangles
                    pomoc = Pomocnik(self.cel)
                    points = pomoc.find(self.screenshot, self.moc_wykrywania, 'rectangles')

                    # lock the thread while updating the results
                    self.lock.acquire()
                    self.rectangles = pomoc.rectangles
                    self.lock.release()











    
