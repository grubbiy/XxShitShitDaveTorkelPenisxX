'''
import pyautogui as pyat
import time
print("Started.")

time.sleep(2)
def pictureExists(file):

def pictureMoveTo(file):
    try:
        pyat.moveTo(pyat.locateOnScreen(file)[0] + (pyat.locateOnScreen(file)[2] / 2),pyat.locateOnScreen(file)[1] + (pyat.locateOnScreen(file)[3] / 2), 2)
        print(f"Moved successfully to picture: {file}")
    except Exception:
        print(f"An error is located in: {file}")
pictureMoveTo('location_dock_station.png')
pictureMoveTo('text.png')
pictureMoveTo('location_activate.png')
pictureMoveTo('ship_activewindow.png')
'''

from PIL import Image
import pytesseract
import pyautogui
import time

#pyautogui.mouseInfo()

for i in range(1,6):
    print(6-i)
    time.sleep(1)

# Angi hvor Tesseract er installert
pytesseract.pytesseract.tesseract_cmd = r"C:\TesseractPY\tesseract.exe"

# Åpne bildet
#image = Image.open("read_overview.png")
#image = pyautogui.screenshot(region=(1495,169,1908,181))
image = pyautogui.screenshot()
image.save("debugimage.png")

# Få detaljert data om all tekst
data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

# Gå gjennom hvert ord
for i in range(len(data['text'])): #Gå gjennom alle ordene som blir funnet
    print(f"Ord: {data['text'][i]}")
    time.sleep(0.05)
    word = data['text'][i]
    if "Aegis" in word.lower():  # Sjekk om "Aegis" finnes
        x = data['left'][i]
        y = data['top'][i]
        w = data['width'][i]
        h = data['height'][i]

        center_x = x + w // 2
        center_y = y + h // 2

        print(f"Fant '{word}' på posisjon: ({center_x}, {center_y})")

        # Flytt musen dit
        pyautogui.moveTo(center_x, center_y, duration=1)
        break
else:
    print(f"Fant ikke 'Aegis' i bildet.")

