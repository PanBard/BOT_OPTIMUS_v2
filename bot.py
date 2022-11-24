import cv2 as cv
import pyautogui
from time import sleep, time
from threading import Thread, Lock, Timer
from math import sqrt
import random
from radio import Nadaj, Odbiornik

class BotState:
    NAMIERZANIE = 0
    MOVING = 1
    KILLING = 0
    SKRZYNKI = 1
    MAPA = 0
    POPRAWKA_MAPY = 0

class Optimus_Logika:
    mojstart = time()
    odswierzanieMapy = time()
    odswierzanieMapyDlaWszystkich = time()
    end = time()
    # threading properties
    stopped = True
    lock = None
    # properties
    
    state = None
    targets = []
    mapson = []
    ikona_mapy = []
    window_offset = (0,0)
    window_w = 0
    window_h = 0
    # lasery = 0
    # rakiety = 0
  
    
    def __init__(self, window_offset, window_size):
        # create a thread lock object
        self.lock = Lock()
        #update
        self.window_offset = window_offset
        self.window_w = window_size[0]
        self.window_h = window_size[1]
        glosnik = Odbiornik()
        glosnik.start()
        Nadaj.INITIALIZING = 1
        sleep(3)
    
    def kil_target(self):
        targety = len(self.targets)

        while targety > 0:
            if self.stopped:
                break

            if self.targets:
                self.targets = self.targets_ordered_by_distance(self.targets)
                target_pos = self.targets[0]
                screen_x, screen_y = self.get_screen_position(target_pos)
                # pyautogui.moveTo(x=screen_x , y=screen_y)

            # pyautogui.press('1')
            # pyautogui.click()
            # pyautogui.press('1')
#            pyautogui.press('2')
            sleep(1)
#            pyautogui.press('2')   
            # self.lasery += 1
            # self.rakiety += 1
            self.end = time()
            # end = time()
            # if (end - self.mojstart)>120:
            #         Nadaj.R_START = 1
            #         pyautogui.moveTo(1128,536)
            #         sleep(1)
            #         pyautogui.click()
            #         sleep(1)
            #         pyautogui.click(18,278)
            #         sleep(1)
            #         pyautogui.click(1323,688)
            #         sleep(1)
            #         Nadaj.R_END = 1
            #         pyautogui.click(1159,594)
            #         sleep(1)
            #         self.mojstart = time()

            # if (end - self.odswierzanieMapy)>20:
            #         Nadaj.MAP = 1
            #         pyautogui.moveTo(1128,536)
            #         sleep(1)
            #         pyautogui.click()
            #         sleep(1)
            #         pyautogui.click(18,278)
            #         sleep(1)
            #         self.odswierzanieMapy = time()
            #         BotState.KILLING = 1
            #         BotState.MOVING = 0
            #         BotState.NAMIERZANIE = 0
            #         self.namierzanie()

            # if lasery == 60:
            #     self.lasery = 0
            #     pyautogui.press('9')
            
            # if rakiety == 100:
            #     self.rakiety = 0
            #     pyautogui.press('8')

            
            BotState.KILLING = 1
            if not self.targets:
                BotState.KILLING = 0
                BotState.NAMIERZANIE = 1
                break

    def namierzanie(self):
        if self.targets:
            self.targets = self.targets_ordered_by_distance(self.targets)
            target_pos = self.targets[0]
            screen_x, screen_y = self.get_screen_position(target_pos)
            # pyautogui.moveTo(x=screen_x , y=screen_y)
            # pyautogui.click()
            # pyautogui.press('1')
            BotState.KILLING = 1
            BotState.NAMIERZANIE = 0
            sleep(3)
        else: BotState.MOVING = 1
        self.end = time()

    def nadajnik(self):
        while not self.targets:
            szerokosc = random.randint(-70,70)
            wysokosc = random.randint(-40,40)
            #pyautogui.click(1242-elo,649-elo) # do slabej mapy
            # pyautogui.click(1240-szerokosc,642-wysokosc) # do silnej mayp
            if self.targets:
                BotState.NAMIERZANIE = 1
                Nadaj.KRONZOWNIK = 0
        
    def get_screen_position(self, pos):
        return (pos[0] + self.window_offset[0], pos[1] + self.window_offset[1])

    def targets_ordered_by_distance(self, targets):
        # our character is always in the center of the screen
        my_pos = (self.window_w / 2, self.window_h / 2)
        def pythagorean_distance(pos):
            return sqrt((pos[0] - my_pos[0])**2 + (pos[1] - my_pos[1])**2)
        targets.sort(key=pythagorean_distance)
        return targets
        
    

    def move(self):
        if not self.targets:   
            # szerokosc = random.randint(-70,70)
            # wysokosc = random.randint(-40,40)
            # #pyautogui.click(1242-elo,649-elo) # do slabej mapy
            # pyautogui.click(1240-szerokosc,642-wysokosc) # do silnej mayp
            # sleep(1)
            Nadaj.KRONZOWNIK = 1
        else:
            BotState.MOVING = 0
            BotState.NAMIERZANIE = 1
        self.end = time()
    def update_targets(self, targets):
        #self.lock.acquire()
        self.targets = targets
        #self.lock.release()
    # threading methods

    def update_mapsony(self, mapsony):
        #self.lock.acquire()
        self.mapson = mapsony
        #self.lock.release()
    # threading methods

    def update_ikona_mapy(self, ikona):
        # self.lock.acquire()
        self.ikona_mapy = ikona
        # self.lock.release()

    # threading methods def update_mapsony(self, mapsony):
    #         #self.lock.acquire()
    #         self.mapson = mapsony
    #         #self.lock.release()
    #     # threading methods

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        Nadaj.stopped = True
        self.stopped = True

    # main logic controller
    def run(self):
        while not self.stopped:

            if BotState.NAMIERZANIE == 1:
                #Nadaj.S_N = 1
                self.namierzanie()
            if BotState.KILLING == 1:
                #Nadaj.S_K = 1
                self.kil_target()
            if BotState.MOVING == 1:
                self.move()
                Nadaj.S_M = 1

            if self.mapson:
                target_pos = self.mapson[0]
                screen_x, screen_y = self.get_screen_position(target_pos)
                pyautogui.moveTo(x=screen_x - 70, y=screen_y)
                BotState.MAPA = 0
                BotState.SKRZYNKI = 1
                print("jest mapa")

            if self.ikona_mapy:
                target_pos = self.ikona_mapy[0]
                screen_x, screen_y = self.get_screen_position(target_pos)
                pyautogui.moveTo(x=screen_x, y=screen_y)
                pyautogui.click()
                print("klik na ikone mapy")
                BotState.POPRAWKA_MAPY = 0
                BotState.SKRZYNKI = 1


            if (self.end - self.odswierzanieMapyDlaWszystkich) > 5:
                    Nadaj.MAP = 1
                    BotState.SKRZYNKI = 0

                    BotState.MAPA = 1
                    sleep(2)
                    if not self.mapson:
                        BotState.MAPA = 0
                        BotState.POPRAWKA_MAPY = 1

                    self.odswierzanieMapyDlaWszystkich = time()
                    BotState.KILLING = 1
                    BotState.MOVING = 0
                    BotState.NAMIERZANIE = 0
                    self.namierzanie()
                    print("minelo 5 sekund")
