import cv2 as cv
import numpy as np
from threading import Thread, Lock
from pomocnikDetektora import Pomocnik


class Detektor:
    # threading properties
    stopped = True
    lock = None
    rectangles = []
    # properties
    cascade = None
    screenshot = None

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

                # do object detection
                rectangles = self.rectangles
                pomoc = Pomocnik('lo.jpg')
                points = pomoc.find(self.screenshot, 0.7, 'rectangles')

                # lock the thread while updating the results
                self.lock.acquire()
                self.rectangles = pomoc.rectangles
                self.lock.release()










    
