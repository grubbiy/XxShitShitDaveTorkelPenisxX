from PIL import Image
import pytesseract
import pyautogui
import time
from abyssattacktype import structureFindr, enemyFindr
from dockedAutomation import dockedButtonFindr
from undockedStndr2 import undockedButtonFindr
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)



print("Finding buttons in docked state.")
dockedButtons = dockedButtonFindr()

print(f"{dockedButtons}\nButtons found, showing the users the buttons that were found.")
for pedo in dockedButtons:
    print(f'Moving to {pedo}')
    pyautogui.moveTo(pedo[1],pedo[2],1)

for button in dockedButtons:
    if button[0] == "Undock":
        print(f'Undocking: {button}.')
        pyautogui.moveTo(button[1],button[2],1)
        pyautogui.click()
        time.sleep(10)
        print(f'Undocked: {button}')
print("Finding buttons in undocked state.")
undockedButtons = undockedButtonFindr()

print(f"{undockedButtons}\nButtons found, showing the users the buttons that were found.")
for pedo in undockedButtons:
    print(f'Moving to {pedo}')
    pyautogui.moveTo(pedo[1],pedo[2],1)
for button in undockedButtons:
    if button[0] == "Activate":
        print(f'Warping to activation point: {button}.')
        pyautogui.moveTo(button[1],button[2],1)
        pyautogui.rightClick()
        for button2 in undockedButtons:
            if button2[0] == "Warp":
                pyautogui.moveTo(button2[1],button2[2],1)
                pyautogui.click()
        time.sleep(10)
        print(f'User should be warped to activation point: {button}')







'''
enemiesLocation = enemyFindr()
structureLocat   ion = structureFindr()

print("\nI found these enemies:")
print(enemiesLocation)
print("\n\nAnd these structures:")
print(structureLocation)

for pedo in structureLocation:
    print(f'Moving to {pedo}')
    pyautogui.moveTo(pedo[1],pedo[2],1)


for button in dockedButtons:
    if button[0] == "Multi":
        print(f'I found you {button}.')
        pyautogui.moveTo(button[1],button[2],1)
'''