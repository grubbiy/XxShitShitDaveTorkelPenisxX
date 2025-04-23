from pyautogui import moveTo

from utils import find_button_position
from utils import click_button
from utils import wait_for_text
from utils import wait_for
from utils import find_phrase_position
import pyautogui, time

def buyFilament():

    print("Opening the Regional Market.")
    click_button("Regional")

    print("Choosing an item to buy.")
    click_button("Station")
    pyautogui.click()
    time.sleep(0.2)

    print("Choosing how many items")
    pyautogui.press('3')
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.5)
    print("Force buy")
    if not wait_for("Yes", timeout=10):
        print("Fant ikke 'Yes'")
    click_button("Yes")

    time.sleep(8)



    print("Går til Inventory")
    if not wait_for("Inventory", timeout=10):
        print("Fant ikke 'Inventory'")
        return
    click_button("Inventory")
    time.sleep(0.3)

    print("Åpner Item Hangar")
    click_button("Item")


    print("Leter etter Filament")
    if not wait_for("Electrical", timeout=10):
        print("Fant ikke 'Electrical'")
        return
    click_button("Electrical")
    print("Fant Filament")

    print("Leter etter skipet ditt")
    if wait_for_text("Punisher", timeout=10):
        user = find_button_position("Punisher")
        if user:
            print("Dra Filament til skipet")
            pyautogui.mouseDown()
            pyautogui.moveTo(user)
            pyautogui.mouseUp()
            print("Flyttet Filament til skip")
            time.sleep(0.3)
            pyautogui.click()
        else:
            print("Fant ikke posisjonen til skipet.")
    else:
        print("Fant ikke 'PenisOst' tekst.")