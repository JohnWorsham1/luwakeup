import pyautogui
import time

def keypress(sleepTime):
    while(True):
        pyautogui.press("volumeup")
        pyautogui.press("volumedown")
        time.sleep(sleepTime * 60)

def main():
    sleepTime = int(input("Please input the amount of time, in minutes, in between button presses: "))
    keypress(sleepTime)

try: 
    main()
except KeyboardInterrupt:
    pass
