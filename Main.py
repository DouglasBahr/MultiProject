"""
Title: Main

Date: 4/1/2020

Author: Sinthrill

Description: This is the main file for this repo 
 
"""

#Python import#e.g. from time import sleep
import time

#Custom imports  #e.g. from file import class as name

#Constants  # e.g. GENERIC_CONSTANT = "Status_Test_String"
THE_FINAL_COUNTDOWN = 10
#Code e.g. class Name():

class Rocket():
    def __init__(self):
        self.countdown = THE_FINAL_COUNTDOWN
        self.run(self.countdown)
        
    def run(self, countdown):
        if countdown != 0:
            print(f"{countdown} until liftoff!")
            countdown -= 1
            time.sleep(1)
            self.run(countdown)
        else:
            print(f"{countdown}...\nblastoff!!!!!")
           
if __name__ == '__main__':
    Rocket = Rocket()