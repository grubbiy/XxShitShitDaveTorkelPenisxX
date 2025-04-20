# controllers/combat_controller.py

from utils import grab_screen, ocr_screen
import pyautogui
import time


class CombatController:
    def __init__(self):
        self.priority_list = [
            "Draining", "Neuting",
            "Webifier", "Webbing",
            "Scrambler", "Disruptor",
            "Cruiser", "Frigate",
            "Drone", "Turret"
        ]

    def find_target(self):
        text = ocr_screen()
        for keyword in self.priority_list:
            if keyword.lower() in text.lower():
                print(f"[CombatController] Fant mål: {keyword}")
                return keyword
        return None

    def attack_target(self):
        # Trykk F1 til F4 (modulene)
        print("[CombatController] Angriper med moduler...")
        for key in ['f1', 'f2', 'f3', 'f4']:
            pyautogui.press(key)
        time.sleep(1)

    def run(self):
        print("[CombatController] Starter kamp...")
        timeout = time.time() + 60  # 1 min kamp før vi gir oss

        while time.time() < timeout:
            target = self.find_target()

            if target:
                # Klikk på mål
                print(f"[CombatController] Klikker på fiende: {target}")
                pyautogui.moveTo(960, 540)  # Midten av skjermen, antar mål er sentrert
                pyautogui.click()
                time.sleep(0.5)

                # Angrip
                self.attack_target()
            else:
                print("[CombatController] Ingen mål funnet. Sjekker igjen...")
                time.sleep(1)

        print("[CombatController] Ferdig med kamp.")

