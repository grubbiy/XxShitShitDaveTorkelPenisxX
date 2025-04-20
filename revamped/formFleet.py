from utils import find_button_position
from utils import click_button
from utils import wait_for_text
from utils import find_phrase_position
import pyautogui, time
#pyautogui.mouseInfo()

def FormFleet():
    '''
    print("Pressing keybinds for Fleet window")
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press('f')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('ctrl')
    print("Fleet window should be opened")
    time.sleep(0.5)
    print("Attempting to form a fleet")
    pyautogui.moveTo(find_phrase_position("Form Fleet"))
    pyautogui.click()
    print("You should now be in a fleet.")
    '''
    print("Åpner Fleet-vindu med hotkey")
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press('f')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('ctrl')

    print("Venter på at 'Form Fleet' skal vises")
    if wait_for_text("Form Fleet", timeout=10):
        pos = find_phrase_position("Form Fleet")
        if pos:
            pyautogui.moveTo(pos)
            pyautogui.click()
            print("Du er nå i en fleet.")
        else:
            print("Fant ikke 'Form Fleet'-knappen selv om teksten dukket opp.")
    else:
        print("Fant ikke 'Form Fleet' innen 10 sekunder.")
