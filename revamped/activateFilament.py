from pyautogui import moveTo

from utils import find_button_position
from utils import click_button
from utils import wait_for_text, wait_for
from utils import find_phrase_position
import pyautogui, time
#pyautogui.mouseInfo()
time.sleep(4)


def activateFilament():
    if not wait_for("Tranquil"):
        print("Fant ikke 'Tranquil'")
    click_button("Tranquil")
    pyautogui.rightClick()
    time.sleep(0.4)
    if not wait_for("Use"):
        print("Fant ikke 'Use'")
    click_button("Use")
    time.sleep(0.5)
    if not wait_for("Activate"):
        print("Fant ikke 'Activate'")
    click_button("Activate")
    time.sleep(10)
    activateGate = find_phrase_position("Abyssal Trace")
    moveTo(activateGate[0],activateGate[1],0.3)
    pyautogui.rightClick()
    time.sleep(1)
    if not wait_for("Activate"):
        print("Fant ikke 'Activate'")
    click_button("Activate")
    time.sleep(3)
    activateElGate = pyautogui.locateOnScreen('activateElFil.png')
    pyautogui.moveTo(activateElGate[0],activateElGate[1],0.5)
    pyautogui.click()