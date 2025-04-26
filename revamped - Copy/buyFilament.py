from pyautogui import moveTo

from utils import find_button_position
from utils import click_button
from utils import wait_for_text
from utils import wait_for
from utils import sendStatus
from utils import find_phrase_position
import pyautogui, time

def buyFilament():

    sendStatus("Opening the Regional Market.")
    if not wait_for("Regional", timeout=50):
        sendStatus("Fant ikke 'Regional'")
        return
    click_button("Regional")

    sendStatus("Choosing an item to buy.")
    if not wait_for("Station", timeout=50):
        sendStatus("Fant ikke 'Station'")
        return
    click_button("Station")
    pyautogui.click()
    time.sleep(4)

    sendStatus("Choosing how many items")
    pyautogui.press('3')
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.5)
    sendStatus("Force buy")
    if not wait_for("Yes", timeout=7):
        sendStatus("Fant ikke 'Yes'")
    click_button("Yes")

    time.sleep(8)



    sendStatus("Går til Inventory")
    if not wait_for("Inventory", timeout=50):
        sendStatus("Fant ikke 'Inventory'")
        return
    click_button("Inventory")
    time.sleep(0.3)

    sendStatus("Åpner Item Hangar")
    if not wait_for("Item", timeout=50):
        sendStatus("Fant ikkje Item Hangar")
        return
    click_button("Item")



    sendStatus("Leter etter Filament")
    if not wait_for("Electrical", timeout=50):
        sendStatus("Fant ikke 'Electrical'")
        return
    click_button("Electrical")
    sendStatus("Fant Filament")

    sendStatus("Leter etter skipet ditt")
    if wait_for_text("Punisher", timeout=50):
        user = find_button_position("Punisher")
        if user:
            sendStatus("Dra Filament til skipet")
            pyautogui.mouseDown()
            pyautogui.moveTo(user)
            pyautogui.mouseUp()
            sendStatus("Flyttet Filament til skip")
            time.sleep(0.3)
            pyautogui.click()
        else:
            sendStatus("Fant ikke posisjonen til skipet.")
    else:
        sendStatus("Fant ikke 'PenisOst' tekst.")