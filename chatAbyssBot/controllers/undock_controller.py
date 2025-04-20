# undock_controller.py
from utils import click_button, wait_for_text, ocr_screen
import time

class UndockController:
    def __init__(self):
        self.undock_button_text = "Undock"
        self.space_indicator_text = "Activate"  # Kan være "Activate Gate", "Abyssal Trace", etc

    def is_docked(self):
        screen_text = ocr_screen()
        return self.undock_button_text.lower() in screen_text.lower()

    def undock(self):
        if self.is_docked():
            print("[📦] Undock-knapp funnet. Klikker...")
            click_button(self.undock_button_text)
            print("[🕒] Venter på å bli undocket...")
            if wait_for_text(self.space_indicator_text, timeout=30):
                print("[✅] Vi er nå undocket og klar for action.")
                return True
            else:
                print("[❌] Timeout – klarte ikkje å undocke.")
                return False
        else:
            print("[⚠️] Undock-knappen finnes ikkje. Kanskje vi allerede er i space?")
            return True  # Safe fallback
