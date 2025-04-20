# controllers/next_room_controller.py

from utils import click_button, wait_for_text
import time

class NextRoomController:
    def __init__(self):
        self.gate_button_text = "Activate Gate"
        self.next_room_text = "Abyssal Trace"  # Tekst som vises når du har kommet til nytt rom (kan justeres)

    def activate_gate(self):
        print("[NextRoomController] Prøver å aktivere rom-gate...")

        success = click_button(self.gate_button_text)
        if success:
            print("[NextRoomController] Klikket på gate! Venter på at nytt rom skal loade...")
            time.sleep(5)
            if wait_for_text(self.next_room_text, timeout=20):
                print("[NextRoomController] Vi er i nytt rom!")
                return True
            else:
                print("[NextRoomController] Vi fikk ikke bekreftet at nytt rom er lastet.")
                return False
        else:
            print("[NextRoomController] Fant ikke gate-knappen.")
            return False
