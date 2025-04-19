from PIL import Image
import pytesseract
import pyautogui
import time
from abyssattacktype import structureFindr, enemyFindr
from dockedAutomation import dockedButtonFindr


dockedButtons = dockedButtonFindr()
for pedo in dockedButtons:
    print(f'Moving to {pedo}')
    pyautogui.moveTo(pedo[1],pedo[2],1)

'''
enemiesLocation = enemyFindr()
structureLocation = structureFindr()

print("\nI found these enemies:")
print(enemiesLocation)
print("\n\nAnd these structures:")
print(structureLocation)

for pedo in structureLocation:
    print(f'Moving to {pedo}')
    pyautogui.moveTo(pedo[1],pedo[2],1)
'''