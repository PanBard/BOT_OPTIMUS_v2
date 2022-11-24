from threading import Thread, Lock
import playsound
from time import sleep
import pyautogui


class Nadaj:
    S_K = 0
    S_M = 0
    S_N = 0
    R_START = 0
    R_END = 0
    MAP = 0
    INITIALIZING = 0
    KRONZOWNIK = 0

    stopped = False
class Odbiornik: 

     # threading properties
    stopped = True
    lock = None

    # properties
    cascade = None
    screenshot = None

    

    def __init__(self):
        # create a thread lock object
        self.lock = Lock()
        
        # load the trained model    

    def autopilot(self):
        while Nadaj.KRONZOWNIK == 1:
            # pyautogui.moveTo(1180,597)
            # sleep(1)
            # pyautogui.click()
            # sleep(20)
            # pyautogui.moveTo(1325,628)
            # sleep(1)
            # pyautogui.click()
            # sleep(20)
            # pyautogui.moveTo(1167,640)
            # sleep(1)
            # pyautogui.click()
            # sleep(20)
            # pyautogui.moveTo(1325,689)
            # sleep(1)
            # pyautogui.click()
            # sleep(20)
            pass


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
        while not Nadaj.stopped:
            if Nadaj.S_K == 1:
                playsound.playsound('komendy/S_K.mp3')
                Nadaj.S_K = 0
                sleep(3)

            elif Nadaj.S_N == 1:
                playsound.playsound('komendy/S_N.mp3')
                Nadaj.S_N = 0
                sleep(2)

            elif Nadaj.S_M == 1:
                playsound.playsound('komendy/S_M.mp3')
                Nadaj.S_M = 0
                sleep(3)
                
            elif Nadaj.R_START == 1:
                playsound.playsound('komendy/R_START.mp3')
                Nadaj.R_START = 0
                sleep(2)

            elif Nadaj.R_END == 1:
                playsound.playsound('komendy/R_END.mp3')
                Nadaj.R_END = 0
                sleep(2)

            elif Nadaj.INITIALIZING == 1:
                playsound.playsound('komendy/INIT.mp3')
                Nadaj.INITIALIZING = 0
                

            elif Nadaj.MAP == 1:
                playsound.playsound('komendy/MAP.mp3')
                Nadaj.MAP = 0
            
            if Nadaj.KRONZOWNIK == 1:
                self.autopilot()
            



            







    
