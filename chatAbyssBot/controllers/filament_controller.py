# filament_controller.py
from utils import click_button, wait_for, ocr_screen
import pyautogui
import time


class FilamentController:
    def __init__(self):
        self.filament_name = "Calm Electrical Filament"

    def check_inventory(self):
        # Åpne Inventory
        click_button("Inventory")
        time.sleep(2)

        # OCR Inventory-vinduet (kan spesifisere region hvis du vil optimalisere)
        inventory_text = ocr_screen()
        if self.filament_name.lower() in inventory_text.lower():
            print("[✓] Filament finnes i inventory.")
            return True
        else:
            print("[✗] Fant ikkje filament. Må kjøpe.")
            return False

    def open_market(self):
        click_button("Market")
        time.sleep(3)
        return wait_for("Search", timeout=10)

    def search_filament(self):
        click_button("Search")
        pyautogui.write(self.filament_name, interval=0.05)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(2)

    def buy_filament(self):
        if not self.open_market():
            print("[ERROR] Kunne ikkje åpne markedet.")
            return False

        self.search_filament()

        # Klikk på resultat (vi antar det øverste resultatet er riktig)
        pyautogui.moveRel(0, 100, duration=0.5)
        pyautogui.click()
        time.sleep(2)

        # Klikk "Buy" og bekreft
        click_button("Buy")
        time.sleep(2)
        click_button("Buy")  # Bekreft kjøpet
        print("[✓] Kjøpte Calm Gamma Filament.")
        time.sleep(2)
        return True

    def ensure_filament(self):
        if not self.check_inventory():
            success = self.buy_filament()
            return success
        return True
