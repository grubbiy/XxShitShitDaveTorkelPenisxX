import pyautogui

from utils import find_button_position, click_button, wait_for_text, wait_for, find_phrase_position, find_pixel_color
from buyFilament import buyFilament
from formFleet import FormFleet
from activateFilament import activateFilament
import time
from abyssattacktype import enemyFindr, structureFindr
from attackSequence import attack_enemies
from utils import sendStatus
#pyautogui.mouseInfo()


sendStatus("Starter bot, venter litt...")
time.sleep(4)



#buyFilament()
FormFleet()

undockPos = pyautogui.locateOnScreen('undock.png')
pyautogui.moveTo(undockPos[0],undockPos[1],0.3)
time.sleep(0.4)
pyautogui.click()
time.sleep(15)


#pyautogui.press('l')
time.sleep(0.4)
if not wait_for("Abyssal"):
    sendStatus("Fant ikke 'Abyssal'")
abyssal = find_button_position("Abyssal")
pyautogui.moveTo(abyssal[0],abyssal[1],0.3)

sendStatus("Leter etter Activate")
if not wait_for("Activate"):
    sendStatus("Fant ikke 'Activate'")
activate = find_button_position("Activate")
pyautogui.moveTo(activate[0],activate[1],0.4)
pyautogui.rightClick()
sendStatus("Leter etter Warp")
if not wait_for("Warp"):
    sendStatus("Fant ikke 'Warp'")
click_button("Warp")

time.sleep(0.5)

pyautogui.moveTo(abyssal[0],abyssal[1],0.3)
pyautogui.click()

for i in range(30, 0, -1):
    sendStatus(i)
    time.sleep(1)
    


activateFilament()

time.sleep(12)
 
sendStatus("Starting propulsion")
pyautogui.keyDown('alt')
pyautogui.keyDown('f1')
pyautogui.keyUp('alt')
pyautogui.keyUp('f1')
time.sleep(0.5)
sendStatus("Starting shields.")
pyautogui.keyDown('ctrl')
pyautogui.keyDown('f2')
pyautogui.keyUp('ctrl')
pyautogui.keyUp('f2')
time.sleep(0.3)

sendStatus("First wave.")
attack_enemies()

sendStatus("Second wave.")
attack_enemies()
sendStatus("Third, last wave.")
attack_enemies()

sendStatus("Bot is finished and is returning to dock for repeated automation.")