from PIL import Image
import pytesseract
import pyautogui
import time
#pyautogui.mouseInfo()


# Hvor Tesseract er installert
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Ta screenshot og lagre for debug

userShip = "penisOst"

# OCR

def fjern_duplikat_navn(liste):
    sett = set()
    ny_liste = []
    for item in liste:
        navn = item[0]
        if navn not in sett:
            ny_liste.append(item)
            sett.add(navn)
    return ny_liste



def undockedButtonFindr():
    options = [userShip, "Items", "Multi", "Ultra", "Gamma", "Activate","Dock"]
    options_ = []

    min_x, max_x = 48, 2000
    min_y, max_y = 51, 1038

    for i in range(5):
        print(f'Starting for the {i+1}. time.')
        image = pyautogui.screenshot()
        data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

        for i in range(len(data['text'])):
            word = data['text'][i].strip()
            for option in options:
                if option.lower() in word.lower():
                    x = data['left'][i]
                    y = data['top'][i]
                    w = data['width'][i]
                    h = data['height'][i]
                    center_x = x + w // 2
                    center_y = y + h // 2

                    #if min_x <= center_x <= max_x and min_y <= center_y <= max_y:
                    options_.append([option, center_x, center_y])

    print(f"Found all words in 5 tries.")

    # Fjern eksakte duplikater
    unique_options = []
    seen = set()

    for option in options_:
        key = (option[0], option[1], option[2])
        if key not in seen:
            unique_options.append(option)
            seen.add(key)

    # Fjern nesten-like duplikater (basert på avstand og navn)
    unique_options = fjern_duplikat_navn(unique_options)

    warpndock = ["Warp","Dock"]
    for button in unique_options:
        if button[0] == "Activate":
            pyautogui.moveTo(button[1],button[2],1)
            pyautogui.rightClick()
            for i in range(2):
                print(f'Starting for the {i + 1}. time.')
                image = pyautogui.screenshot()
                data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

                for i in range(len(data['text'])):
                    word = data['text'][i].strip()
                    for option in (warpndock):
                        if option.lower() in word.lower():
                            x = data['left'][i]
                            y = data['top'][i]
                            w = data['width'][i]
                            h = data['height'][i]
                            center_x = x + w // 2
                            center_y = y + h // 2

                            # if min_x <= center_x <= max_x and min_y <= center_y <= max_y:
                            unique_options.append([option, center_x, center_y])

    unique_options = fjern_duplikat_navn(unique_options)

    activatex, activatey, warpx, warpy = 0,0,0,0
    for outputs in unique_options:
        if outputs == "Activate":
            activatex, activatey = outputs[1],outputs[2]
    for outputs in unique_options:
        if outputs == "Warp":
            warpx, warpy = outputs[1],outputs[2]
    differencex, differencey = activatex-warpx,activatey-warpy

    dockx,docky,dockwx,dockwy = 0,0,0,0

    for outputs in unique_options:
        if outputs == "Dock":
            dockx,docky = outputs[1],outputs[2]
            dockwx = dockx + differencex
            dockwy = docky + differencey

    unique_options.append(["DockW",dockwx,dockwy])


    return unique_options
