# controllers/loot_controller.py

from utils import click_button
import pyautogui
import time

class LootController:
    def __init__(self):
        self.loot_words = ["Loot All", "Open Cargo", "Cargo Container"]

    def find_and_loot(self):
        print("[LootController] Leter etter loot...")

        for word in self.loot_words:
            if click_button(word):
                print(f"[LootController] Fant og åpnet: {word}")
                time.sleep(2)  # Vent litt på at loot-vinduet åpnes
                pyautogui.hotkey('ctrl', 'a')  # Merk alt (for sikkerhet)
                pyautogui.press('ctrl')        # Kan trigge "Loot All" via tast
                time.sleep(0.5)
                pyautogui.press('esc')         # Lukk vinduet
                return True

        print("[LootController] Fant ingenting å loote.")
        return False
