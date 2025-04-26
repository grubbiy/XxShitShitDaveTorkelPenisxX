from utils import find_button_position
from utils import click_button
from utils import wait_for_text
from utils import find_phrase_position
import pyautogui, time
from utils import sendStatus
#pyautogui.mouseInfo()

def FormFleet():
    '''
    sendStatus("Pressing keybinds for Fleet window")
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press('f')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('ctrl')
    sendStatus("Fleet window should be opened")
    time.sleep(0.5)
    sendStatus("Attempting to form a fleet")
    pyautogui.moveTo(find_phrase_position("Form Fleet"))
    pyautogui.click()
    sendStatus("You should now be in a fleet.")
    '''
    sendStatus("Åpner Fleet-vindu med hotkey")
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press('f')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('ctrl')

    sendStatus("Venter på at 'Form Fleet' skal vises")
    if wait_for_text("Form Fleet", timeout=50):
        pos = find_phrase_position("Form Fleet")
        if pos:
            pyautogui.moveTo(pos)
            pyautogui.click()
            sendStatus("Du er nå i en fleet.")
        else:
            sendStatus("Fant ikke 'Form Fleet'-knappen selv om teksten dukket opp. Prøver på ny")
        while not pos:
            sendStatus("Fant ikkje pos, prøver på ny til det finst.")
            pos = find_phrase_position("Form Fleet")
            if pos:
                pyautogui.moveTo(pos)
                pyautogui.click()
                sendStatus("Du er nå i en fleet.")
            else:
                sendStatus("Fant ikke 'Form Fleet'-knappen selv om teksten dukket opp. Prøver på ny")

    else:
        sendStatus("Fant ikke 'Form Fleet' innen 30 sekunder.")
