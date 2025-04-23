import time
import pyautogui
from abyssattacktype import enemyFindr, structureFindr
from utils import click_button
print("Attacking phase.")
def attack_enemies():
    '''
    while enemies:
        for enemy in enemies:
            # Klikk på fienden for å targete
            print(f'Moving mouse to enemy: {enemy}')
            pyautogui.moveTo(enemy[1], enemy[2], duration=0.3)
            
            # W + Click = orbit(500m)
            # CTRL + Click = Target
            print("Pressing buttons for attacking.")
            pyautogui.keyDown('w')
            pyautogui.click()
            time.sleep(0.4)
            pyautogui.keyUp('w')

            # Beveg deg nærme (her må du implementere bevegelseslogikk)
            # For eksempel, trykk på en tast for å aktivere afterburner eller lignende

            pyautogui.keyDown('alt')
            pyautogui.keyDown('f1')
            time.sleep(0.2)
            pyautogui.keyUp('alt')
            pyautogui.keyUp('f1')
            time.sleep(0.1)
            print("Propulsion activated.")

            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('f2')
            time.sleep(0.2)
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('f2')
            time.sleep(0.1)
            print("Amour module activated.")


            time.sleep(14)  # Vent til du er nærme

            print("Targetting enemies.")
            pyautogui.keyDown('ctrl')
            pyautogui.click()
            time.sleep(0.4)
            pyautogui.keyUp('ctrl')
            print("Enemies targetted.")

            # Begynn å skyte
            print("Starting to shoot.")
            pyautogui.press('f1')  # Eksempel: aktiver våpen
            time.sleep(5)  # Vent litt før du sjekker om fienden er død

            # Sjekk om fienden fortsatt er der
            print("Checking for change in enemies.")
            new_enemies = enemyFindr()
            while len(new_enemies) == len(enemies):
                # Fienden er fortsatt der, vent litt til
                print("Same old enemies.")
                time.sleep(5)
            # Fienden er eliminert
            print("New enemies.")
            # Oppdater fiendelisten
            enemies = enemyFindr()
            '''
    print("Setting tries.")
    tries = 0
    print("Initializing enemy list.")
    enemies = []
    while True:
        print("Fetching enemies.")
        enemies = enemyFindr()
        tries +=1

        if not enemies:
            print("No enemies found.")
            break

        print(f'Moving to first enemy position: {enemies[0]}')
        if tries == 1:
            print("Moving closer since its the first time.")
            pyautogui.moveTo(enemies[0][1],enemies[0][2],0.3)
            pyautogui.keyDown('w')
            pyautogui.click()
            pyautogui.keyUp('w')
            print("Starting countdown for moving closer.")
            for i in range(13,0,-1):
                print(i)

        print("Orbiting enemy for attack.")
        pyautogui.moveTo(enemies[0][1],enemies[0][2],0.3)
        pyautogui.keyDown('w')
        pyautogui.click()
        pyautogui.keyUp('w')
        time.sleep(1)

        print("Targetting the enemy.")
        pyautogui.keyDown('ctrl')
        pyautogui.click()
        pyautogui.keyUp('ctrl')

        time.sleep(4)

        print("Starting the turret.")
        pyautogui.press('f1')

        pyautogui.moveTo(pyautogui.position()[0]-200,pyautogui.position()[1]-200)

        print("Enemy check running.")
        newEnemiesCheck = enemyFindr()
        checks_ = 0
        print("Loop for checking new enemies initiated.")
        while enemies == newEnemiesCheck:
            print(f'Waiting for an enemy to die. {checks_} checks.')
            checks_ += 1
            newEnemiesCheck = enemyFindr()



    print("No more enemies found, looking for structures.")


    # Når alle fiender er eliminert, finn strukturer
    print("Checking for structures.")
    structures = structureFindr()
    print(f'Structures are found: {structures}')
    rekkefølge = 1

    while True:
        for structure in structures:
            if rekkefølge == 1:
                if structure[0] == 'Biocomb':
                    print(f'I would like to go to: {structure}')
                    pyautogui.moveTo(structure[1],structure[2],0.4)
                    pyautogui.keyDown('q')
                    pyautogui.click()
                    pyautogui.keyUp('q')
                    time.sleep(8)
                    print("Here there would be a function to open up the loot and loot it, we are not there yet.")
                    rekkefølge += 1
            if rekkefølge == 2:
                if structure[0] == 'Transfer':
                    print(f'I would like to go to: {structure}')
                    pyautogui.moveTo(structure[1], structure[2], 0.4)
                    pyautogui.keyDown('d')
                    pyautogui.click()
                    pyautogui.keyUp('d')
                    time.sleep(15)
                    break
                elif structure[0] == 'Origin':
                    print(f'I would like to go to: {structure}')
                    pyautogui.moveTo(structure[1], structure[2], 0.4)
                    pyautogui.keyDown('d')
                    pyautogui.click()
                    pyautogui.keyUp('d')
                    time.sleep(15)
                    break
