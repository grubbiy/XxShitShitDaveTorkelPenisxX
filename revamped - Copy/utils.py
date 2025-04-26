# utils.py
import pyautogui
import pytesseract
import time
import cv2
import numpy as np
from PIL import ImageGrab
import requests


# Sett pytesseract path hvis nødvendig
pytesseract.pytesseract.tesseract_cmd = r'PyTesseract\tesseract.exe'
print("PyTesseract set up.")


def sendStatus(message):
    print(message)



def grab_screen(region=None):
    img = ImageGrab.grab(bbox=region)
    return cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

def ocr_screen(region=None):
    screen = grab_screen(region)
    text = pytesseract.image_to_string(screen)
    return text

def click_button(text_to_find, region=None, confidence=0.7):
    screen = grab_screen(region)
    gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

    for i, word in enumerate(data['text']):
        if text_to_find.lower() in word.lower():
            x = data['left'][i] + data['width'][i] // 2
            y = data['top'][i] + data['height'][i] // 2
            pyautogui.moveTo(x, y, duration=0.3)
            pyautogui.click()
            return True
    return False

def find_button_position(text_to_find, region=None):
    screen = grab_screen(region)
    gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

    for i, word in enumerate(data['text']):
        if text_to_find.lower() in word.lower():
            x = data['left'][i] + data['width'][i] // 2
            y = data['top'][i] + data['height'][i] // 2
            return (x, y)  # <- Bare returnerer koordinatene
    return None


def wait_for(text, timeout=50, region=None):
    start = time.time()
    while time.time() - start < timeout:
        if click_button(text, region=region):
            return True
        time.sleep(1)
    return False

def wait_for_text(text, timeout=50, region=None):
    start = time.time()
    while time.time() - start < timeout:
        screen_text = ocr_screen(region)
        if text.lower() in screen_text.lower():
            return True
        time.sleep(1)
    return False

def find_pixel_color(target_rgb, region=None):
    """
    Søk etter en spesifikk RGB-farge på skjermen (eller i region).
    Returnerer (x, y) posisjon hvis funnet, ellers None.
    """
    img = grab_screen(region)
    height, width, _ = img.shape

    for y in range(height):
        for x in range(width):
            pixel = img[y, x]
            if tuple(pixel) == target_rgb:
                if region:
                    # Juster x, y til global posisjon hvis region er spesifisert
                    x += region[0]
                    y += region[1]
                return (x, y)
    return None

def find_phrase_position(phrase, region=None):
    screen = grab_screen(region)
    gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

    words = data['text']
    phrase_words = phrase.lower().split()

    for i in range(len(words) - len(phrase_words) + 1):
        match = True
        for j, pw in enumerate(phrase_words):
            if pw not in words[i + j].lower():
                match = False
                break

        if match:
            x = data['left'][i] + data['width'][i] // 2
            y = data['top'][i] + data['height'][i] // 2
            return x, y

    return None
