import pyautogui

from utils import find_button_position, click_button, wait_for_text, wait_for, find_phrase_position, find_pixel_color
from buyFilament import buyFilament
from formFleet import FormFleet
from activateFilament import activateFilament
import time
from abyssattacktype import enemyFindr, structureFindr
#pyautogui.mouseInfo()


print("Starter bot, venter litt...")
time.sleep(4)



buyFilament()
FormFleet()

undockPos = pyautogui.locateOnScreen('undock.png')
pyautogui.moveTo(undockPos[0],undockPos[1],0.3)
time.sleep(0.4)
pyautogui.click()
time.sleep(15)


#pyautogui.press('l')
time.sleep(0.4)
if not wait_for("Abyssal", timeout=10):
    print("Fant ikke 'Abyssal'")
click_button("Abyssal")

print("Leter etter Activate")
if not wait_for("Activate", timeout=10):
    print("Fant ikke 'Activate'")
activate = find_button_position("Activate")
pyautogui.moveTo(activate[0],activate[1],0.4)
pyautogui.rightClick()
print("Leter etter Warp")
if not wait_for("Warp", timeout=10):
    print("Fant ikke 'Warp'")
click_button("Warp")

time.sleep(0.5)
if not wait_for("Abyssal", timeout=10):
    print("Fant ikke 'Abyssal'")
click_button("Abyssal")
for i in range(30, 0, -1):
    print(i)
    time.sleep(1)

activateFilament()

time.sleep(12)

currentEnemies = enemyFindr()
