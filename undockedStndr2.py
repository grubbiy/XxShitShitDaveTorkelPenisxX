from PIL import Image
import pytesseract
import pyautogui
import time

# Oppgi sti til Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

userShip = "penisOst"

def fjern_duplikat_navn(liste):
    sett = set()
    ny_liste = []
    for item in liste:
        if item[0] not in sett:
            ny_liste.append(item)
            sett.add(item[0])
    return ny_liste

def undockedButtonFindr():
    options_to_find = [userShip, "Items", "Multi", "Ultra", "Gamma", "Activate", "Dock"]
    extra_options_to_find = ["Warp", "Dock"]

    found_buttons = []

    # Søk etter knapper med OCR
    for i in range(5):
        print(f'Starting OCR scan {i + 1}/5.')
        image = pyautogui.screenshot()
        data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

        for j in range(len(data['text'])):
            word = data['text'][j].strip()
            for option in options_to_find:
                if option.lower() in word.lower():
                    x, y = data['left'][j], data['top'][j]
                    w, h = data['width'][j], data['height'][j]
                    center_x, center_y = x + w // 2, y + h // 2
                    found_buttons.append([option, center_x, center_y])

    print("Finished initial OCR scanning.")
    found_buttons = fjern_duplikat_navn(found_buttons)

    # Hent Warp/Dock frå høyreklikkmeny viss Activate finnes
    activate = next((b for b in found_buttons if b[0] == "Activate"), None)
    if activate:
        pyautogui.moveTo(activate[1], activate[2], 1)
        pyautogui.rightClick()
        time.sleep(0.5)

        for i in range(2):
            print(f'OCR scan of right-click menu {i + 1}/2.')
            image = pyautogui.screenshot()
            data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

            for j in range(len(data['text'])):
                word = data['text'][j].strip()
                for option in extra_options_to_find:
                    if option.lower() in word.lower():
                        x, y = data['left'][j], data['top'][j]
                        w, h = data['width'][j], data['height'][j]
                        center_x, center_y = x + w // 2, y + h // 2
                        found_buttons.append([option, center_x, center_y])

    found_buttons = fjern_duplikat_navn(found_buttons)

    # Kalkuler DockW basert på Warp → Activate-vektor
    activate = next((b for b in found_buttons if b[0] == "Activate"), None)
    warp = next((b for b in found_buttons if b[0] == "Warp"), None)
    dock = next((b for b in found_buttons if b[0] == "Dock"), None)

    if activate and warp and dock:
        diff_x = activate[1] - warp[1]
        diff_y = activate[2] - warp[2]
        dockw_x = dock[1] + diff_x
        dockw_y = dock[2] + diff_y
        found_buttons.append(["DockW", dockw_x, dockw_y])
        print("La til DockW basert på posisjonene.")
    else:
        print("Kunne ikkje lage DockW. Mangler Activate, Warp eller Dock.")

    return found_buttons
