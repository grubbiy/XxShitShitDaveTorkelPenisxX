from PIL import Image
import pytesseract
import pyautogui
import time
#pyautogui.mouseInfo()
# Vent litt før screenshot


# Hvor Tesseract er installert
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Ta screenshot og lagre for debug


# OCR

def enemyFindr():

    # Liste over fiender vi vil finne
    enemy_names = ["Aegis", "Strikeneedle", "Damavik", "Lancer"]


    # Her lagres resultatet
    attackEnemies = []

    min_x, max_x = 1598, 1716
    min_y, max_y = 186, 354

    # Gå gjennom alle ord
    for i in range(5):
        print(f'Starting for the {i+1}. time.')
        image = pyautogui.screenshot()
        image.save("debugimage.png")

        data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

        for i in range(len(data['text'])):
            word = data['text'][i].strip()

            for enemy in enemy_names:
                if enemy.lower() in word.lower():
                    x = data['left'][i]
                    y = data['top'][i]
                    w = data['width'][i]
                    h = data['height'][i]

                    center_x = x + w // 2
                    center_y = y + h // 2

                    # Filtrér ut alt utenfor området
                    if min_x <= center_x <= max_x and min_y <= center_y <= max_y:
                        propulsion = 1 if enemy in ["Aegis", "Lancer"] else 0
                        attackEnemies.append([enemy, center_x, center_y, propulsion])
                        #print(f"Funnet {enemy} på ({center_x}, {center_y})")
    print("Found all words in x tries.")
    # Debug: Vis hele lista
    '''print("\nFiender funnet før sletting av duplikat:")
    for enemy in attackEnemies:
        print(enemy)
        pyautogui.moveTo(enemy[1],enemy[2], 0.3)
    '''
    # Fjern duplikater etterpå
    unique_attackEnemies = []
    seen = set()

    for enemy in attackEnemies:
        # Vi bruker en "tuple" fordi det kan hashes
        key = (enemy[0], enemy[1], enemy[2])

        if key not in seen:
            unique_attackEnemies.append(enemy)
            seen.add(key)
    '''print("\nFiender etter sletting av duplikat:")
    for enemy in unique_attackEnemies:
        print(enemy)
        pyautogui.moveTo(enemy[1],enemy[2], 0.3)'''
    return unique_attackEnemies

def structureFindr():
    staticStructure = ["Biocomb", "Origin", "Transfer"]
    # Her lagres resultatet
    structureAttack = []

    min_x, max_x = 1598, 1716
    min_y, max_y = 186, 354

    # Gå gjennom alle ord
    for i in range(5):
        print(f'Started for the {i+1}. time.')
        image = pyautogui.screenshot()
        image.save("debugimage.png")

        data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

        for i in range(len(data['text'])):
            word = data['text'][i].strip()

            for static in staticStructure:
                if static.lower() in word.lower():
                    x = data['left'][i]
                    y = data['top'][i]
                    w = data['width'][i]
                    h = data['height'][i]

                    center_x = x + w // 2
                    center_y = y + h // 2

                    # Filtrér ut alt utenfor området
                    if min_x <= center_x <= max_x and min_y <= center_y <= max_y:
                        structureAttack.append([static, center_x, center_y])
                        #print(f"Funnet {static} på ({center_x}, {center_y})")
    print("All words found in x times.")
    # Debug: Vis hele lista
    '''print("\nStatisk funnet før sletting av duplikat:")
    for static in structureAttack:
        print(static)
        pyautogui.moveTo(static[1], static[2], 0.3)
    '''
    # Fjern duplikater etterpå
    unique_structureAttack = []
    seen = set()

    for static in structureAttack:
        # Vi bruker en "tuple" fordi det kan hashes
        key = (static[0], static[1], static[2])

        if key not in seen:
            unique_structureAttack.append(static)
            seen.add(key)
    '''print("\nStatisk etter sletting av duplikat:")
    for static in unique_structureAttack:
        print(static)
        pyautogui.moveTo(static[1], static[2], 0.3)'''

    return unique_structureAttack

