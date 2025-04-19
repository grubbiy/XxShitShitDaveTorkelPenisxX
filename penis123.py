from PIL import Image
import pytesseract
import pyautogui
import time
from abyssattacktype import structureFindr, enemyFindr
from dockedAutomation import dockedButtonFindr
from undockedStndr2 import undockedButtonFindr

# Nedtelling før start
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

# Docked-knappesøk
print("Finding buttons in docked state.")
dockedButtons = dockedButtonFindr()
print(f"{dockedButtons}\nButtons found, showing the user the buttons that were found.")

# Visual feedback og klikking
for button in dockedButtons:
    print(f'Moving to {button}')
    pyautogui.moveTo(button[1], button[2], 1)
    if button[0] == "Undock":
        print(f'Undocking: {button}.')
        pyautogui.click()
        time.sleep(10)  # Vente på at undock skjer
        print(f'Undocked: {button}')

# Undocked-knappesøk
print("Finding buttons in undocked state.")
undockedButtons = undockedButtonFindr()
print(f"{undockedButtons}\nButtons found, showing the user the buttons that were found.")

# Visual feedback og warp
for button in undockedButtons:
    print(f'Moving to {button}')
    pyautogui.moveTo(button[1], button[2], 1)

# Warp via Activate → right-click → Warp
activate_button = next((b for b in undockedButtons if b[0] == "Activate"), None)
warp_button = next((b for b in undockedButtons if b[0] == "Warp"), None)

if activate_button and warp_button:
    print(f'Warping to activation point: {activate_button}.')
    pyautogui.moveTo(activate_button[1], activate_button[2], 1)
    pyautogui.rightClick()
    time.sleep(0.5)
    pyautogui.moveTo(warp_button[1], warp_button[2], 1)
    pyautogui.click()
    time.sleep(10)
    print(f'User should be warped to activation point: {activate_button}')
else:
    print("Fant ikkje Activate eller Warp-knappen.")
