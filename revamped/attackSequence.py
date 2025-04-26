import time
import pyautogui
from abyssattacktype import enemyFindr, structureFindr
from utils import click_button
from utils import sendStatus

def attack_enemies():
    sendStatus("Attacking phase.")
    '''
    while enemies:
        for enemy in enemies:
            # Klikk på fienden for å targete
            sendStatus(f'Moving mouse to enemy: {enemy}')
            pyautogui.moveTo(enemy[1], enemy[2], duration=0.3)
            
            # W + Click = orbit(500m)
            # CTRL + Click = Target
            sendStatus("Pressing buttons for attacking.")
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
            sendStatus("Propulsion activated.")

            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('f2')
            time.sleep(0.2)
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('f2')
            time.sleep(0.1)
            sendStatus("Amour module activated.")


            time.sleep(14)  # Vent til du er nærme

            sendStatus("Targetting enemies.")
            pyautogui.keyDown('ctrl')
            pyautogui.click()
            time.sleep(0.4)
            pyautogui.keyUp('ctrl')
            sendStatus("Enemies targetted.")

            # Begynn å skyte
            sendStatus("Starting to shoot.")
            pyautogui.press('f1')  # Eksempel: aktiver våpen
            time.sleep(5)  # Vent litt før du sjekker om fienden er død

            # Sjekk om fienden fortsatt er der
            sendStatus("Checking for change in enemies.")
            new_enemies = enemyFindr()
            while len(new_enemies) == len(enemies):
                # Fienden er fortsatt der, vent litt til
                sendStatus("Same old enemies.")
                time.sleep(5)
            # Fienden er eliminert
            sendStatus("New enemies.")
            # Oppdater fiendelisten
            enemies = enemyFindr()
            '''
    sendStatus("Setting tries.")
    tries = 0
    sendStatus("Initializing enemy list.")
    enemies = []
    while True:
        sendStatus("Fetching enemies.")
        enemies = enemyFindr()
        tries +=1

        if not enemies:
            sendStatus("No enemies found.")
            break

        sendStatus(f'Moving to first enemy position: {enemies[0]}')
        if tries == 1:
            sendStatus("Moving closer since its the first time.")
            pyautogui.moveTo(enemies[0][1],enemies[0][2],0.3)
            pyautogui.keyDown('w')
            pyautogui.click()
            pyautogui.keyUp('w')
            sendStatus("Starting countdown for moving closer.")
            for i in range(13,0,-1):
                time.sleep(1)
                sendStatus(i)

        sendStatus("Orbiting enemy for attack.")
        pyautogui.moveTo(enemies[0][1],enemies[0][2],0.3)
        pyautogui.keyDown('w')
        pyautogui.click()
        pyautogui.keyUp('w')
        time.sleep(1)

        sendStatus("Targetting the enemy.")
        pyautogui.keyDown('ctrl')
        pyautogui.click()
        pyautogui.keyUp('ctrl')

        time.sleep(4)

        sendStatus("Starting the turret.")
        pyautogui.press('f1')

        pyautogui.moveTo(pyautogui.position()[0]-200,pyautogui.position()[1]-200)

        sendStatus("Enemy check running.")
        newEnemiesCheck = enemyFindr()
        checks_ = 0
        sendStatus("Loop for checking new enemies initiated.")
        while enemies == newEnemiesCheck:
            sendStatus(f'Waiting for an enemy to die. {checks_} checks.')
            checks_ += 1
            newEnemiesCheck = enemyFindr()



    sendStatus("No more enemies found, looking for structures.")


    # Når alle fiender er eliminert, finn strukturer
    sendStatus("Checking for structures.")
    structures = structureFindr()
    sendStatus(f'Structures are found: {structures}')
    rekkefølge = 1

    while True:
        for structure in structures:
            if rekkefølge == 1:
                if structure[0] == 'Biocomb':
                    sendStatus(f'I would like to go to: {structure}')
                    pyautogui.moveTo(structure[1],structure[2],0.4)
                    pyautogui.keyDown('q')
                    pyautogui.click()
                    pyautogui.keyUp('q')
                    time.sleep(8)
                    sendStatus("Here there would be a function to open up the loot and loot it, we are not there yet.")
                    time.sleep(1)
                    pyautogui.keyDown('ctrl')
                    pyautogui.click()
                    pyautogui.keyUp('ctrl')
                    time.sleep(4)
                    pyautogui.press('f1')
                    time.sleep(6)
                    input("Press enter for this is not finished (:")
                    #  structures = structureFindr() -- I would use this, but I am not here yet, so I let this be.
                    time.sleep(3)
                    rekkefølge += 1
                    break
            if rekkefølge == 2:
                if structure[0] != 'Biocomb':
                    sendStatus(f'I would like to go to: {structure}')
                    pyautogui.moveTo(structure[1], structure[2], 0.4)
                    pyautogui.keyDown('d')
                    pyautogui.click()
                    pyautogui.keyUp('d')
                    time.sleep(20)
                    break
                    '''
                elif structure[0] == 'Origin':
                    sendStatus(f'I would like to go to: {structure}')
                    pyautogui.moveTo(structure[1], structure[2], 0.4)
                    pyautogui.keyDown('d')
                    pyautogui.click()
                    pyautogui.keyUp('d')
                    time.sleep(20)
                    break
                    '''