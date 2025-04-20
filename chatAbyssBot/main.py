# main.py

import time
from controllers.filament_controller import FilamentController
from controllers.undock_controller import UndockController
from controllers.next_room_controller import NextRoomController
from controllers.combat_controller import CombatController
from controllers.loot_controller import LootController

def main():
    print("[Main] Starter Abyssal Deadspace bot...")

    # 1. Kjøp filament hvis nødvendig
    filament_controller = FilamentController()
    if not filament_controller.check_and_buy_filament():
        print("[Main] Feil ved kjøp av filament. Avslutter.")
        return

    # 2. Undock fra stasjon
    undock_controller = UndockController()
    if not undock_controller.undock():
        print("[Main] Feil ved undocking. Avslutter.")
        return

    # 3. Kombat: Finn og bekjemp fiender
    combat_controller = CombatController()
    if not combat_controller.fight_enemies():
        print("[Main] Feil i kamp. Avslutter.")
        return

    # 4. Loot fiender
    loot_controller = LootController()
    if not loot_controller.loot_enemies():
        print("[Main] Feil ved looting. Avslutter.")
        return

    # 5. Aktiver gate og gå til neste rom
    next_room_controller = NextRoomController()
    if not next_room_controller.activate_gate():
        print("[Main] Feil ved aktivering av gate. Avslutter.")
        return

    print("[Main] Bot har fullført Abyssal Deadspace-rommet.")

if __name__ == "__main__":
    main()
