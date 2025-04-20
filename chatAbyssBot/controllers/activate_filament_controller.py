# controllers/activate_filament_controller.py
import pyautogui
from utils import click_button, wait_for_text, wait_for
import time

class ActivateFilamentController:
    def __init__(self, filament_name="Gamma"):
        self.filament_name = filament_name

    def run(self):
        print(f"[ActivateFilamentController] Starter aktivering av {self.filament_name}-filament...")

        # 1. Klikk på filamentet i inventory
        print("[ActivateFilamentController] Prøver å klikke på filamentet i inventory...")
        if not click_button(self.filament_name):
            print(f"[ActivateFilamentController] Fant ikkje '{self.filament_name}' i inventory.")
            return False

        time.sleep(1)

        # 2. Høyreklikk filamentet
        print("[ActivateFilamentController] Høyreklikker filamentet...")
        click_button(self.filament_name)  # Venstreklikk først for å fokusere
        pyautogui.rightClick()            # Så høyreklikk

        time.sleep(1)

        # 3. Klikk "Activate Filament"
        print("[ActivateFilamentController] Prøver å aktivere filamentet...")
        if not wait_for("Activate Filament", timeout=10):
            print("[ActivateFilamentController] Fant ikkje 'Activate Filament'-valg.")
            return False

        time.sleep(2)

        # 4. Klikk "Enter Abyssal"
        print("[ActivateFilamentController] Klikker 'Enter Abyssal'...")
        if not wait_for("Enter Abyssal", timeout=10):
            print("[ActivateFilamentController] Fant ikkje 'Enter Abyssal'-knappen.")
            return False

        # 5. Vent til vi er inne (Undock-knapp forsvinner = vi ikkje er i station)
        print("[ActivateFilamentController] Venter på at vi skal komme inn i Abyss...")
        start_time = time.time()
        while time.time() - start_time < 30:
            if not wait_for_text("Undock", timeout=2):
                print("[ActivateFilamentController] Vi er inne i Abyss!")
                return True
            time.sleep(1)

        print("[ActivateFilamentController] Timeout: Vi kom ikkje inn i Abyss.")
        return False
