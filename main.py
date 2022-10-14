import random
import time
import textwrap
import shutil
import string
import re

# Vérifie que le module Colorama est présent
try:
    from colorama import init, Fore, Back, Style
    init()
except ModuleNotFoundError:
    raise ModuleNotFoundError("""
    ////////////////////////////////////////////////////////////////////////////////
    Il vous faut le module Colorama pour lancer ce programme. (pip install colorama)
    ////////////////////////////////////////////////////////////////////////////////
    """)
    

SIZE = shutil.get_terminal_size()
TERMINAL_WIDTH = SIZE.columns

COLORS = {
    "B": Fore.BLUE + "B" + Style.RESET_ALL,  # BLUE
    "G": Fore.GREEN + "G" + Style.RESET_ALL,  # GREEN
    "R": Fore.RED + "R" + Style.RESET_ALL,  # RED
    "Y": Fore.YELLOW + "Y" + Style.RESET_ALL,  # YELLOW
    "C": Fore.CYAN + "C" + Style.RESET_ALL,  # CYAN
    "P": Fore.MAGENTA + "P" + Style.RESET_ALL  # PURPLE
}

TEAM_NAMES = {
    Fore.BLUE + "PROJECT COORDINATOR" + Style.RESET_ALL: Fore.BLUE + "Maryse Pilote" + Style.RESET_ALL,
    Fore.GREEN + "QUALITY CONTROL" + Style.RESET_ALL: Fore.GREEN + "Sam Sebille" + Style.RESET_ALL,
    Fore.YELLOW + "LEAD DESIGNER" + Style.RESET_ALL: Fore.YELLOW + "Yanni Haddar" + Style.RESET_ALL,
    Fore.RED + "LEAD PROGRAMMER" + Style.RESET_ALL: Fore.RED + "Quentin Gastaldo" + Style.RESET_ALL
}

CODE_SIZE = 4
allowed_chars = string.printable + " "


# Centrage du texte pour l 'affichage
def center_print(txt, offset = 0, jumpline = True):
    #definition et supression des codes de style ansi
    regex = re.compile("\x1b\[([0-9,A-Z]{1,2}(;[0-9]{1,2})?(;[0-9]{3})?)?[m|K]?", re.UNICODE)
    cleaned_string = re.sub(regex, '', txt)

    #calcul de la longueur finale de la string
    length = len(cleaned_string)

    #ajout d'espaces pour centrer le texte dans la console, en ne prenant en compte que les charactères qui seront affichés
    whitespace = ""
    for space in range((TERMINAL_WIDTH // 2) - (length//2) + offset):
        whitespace = whitespace + " "

    #print les espaces, la string, et enlever les couleurs a la fin
    print(whitespace + txt + Style.RESET_ALL, end = "")

    if jumpline:
        print()


# Affichage du Titre
def start():
    print()
    txt_logo = (Fore.BLUE   + "    ██\      ██\  ██████\   ██████\  ████████\ ████████\ ███████\  ██\      ██\ ██████\ ██\   ██\ ███████\ \n" +
                Fore.BLUE   + "    ███\    ███ |██  __██\ ██  __██\ \__██  __|██  _____|██  __██\ ███\    ███ |\_██  _|███\  ██ |██  __██\ \n" +
                Fore.GREEN  + "    ████\  ████ |██ /  ██ |██ /  \__|   ██ |   ██ |      ██ |  ██ |████\  ████ |  ██ |  ████\ ██ |██ |  ██ |\n" +
                Fore.GREEN  + "    ██\██\██ ██ |████████ |\██████\     ██ |   █████\    ███████  |██\██\██ ██ |  ██ |  ██ ██\██ |██ |  ██ |\n" +
                Fore.YELLOW + "    ██ \███  ██ |██  __██ | \____██\    ██ |   ██  __|   ██  __██< ██ \███  ██ |  ██ |  ██ \████ |██ |  ██ |\n" +
                Fore.YELLOW + "    ██ |\█  /██ |██ |  ██ |██\   ██ |   ██ |   ██ |      ██ |  ██ |██ |\█  /██ |  ██ |  ██ |\███ |██ |  ██ |\n" +
                Fore.RED    + "    ██ | \_/ ██ |██ |  ██ |\██████  |   ██ |   ████████\ ██ |  ██ |██ | \_/ ██ |██████\ ██ | \██ |███████  |\n" +
                Fore.RED    + "    \__|     \__|\__|  \__| \______/    \__|   \________|\__|  \__|\__|     \__|\______|\__|  \__|\_______/\n")

    for line in textwrap.wrap(txt_logo, width=116, drop_whitespace=False):
        center_print(line)

    print()
    center_print(Fore.BLACK + Style.BRIGHT + "Developed by" + Fore.YELLOW + " StackNoodles™")
    center_print(Style.BRIGHT + Fore.BLACK + "This work is licensed under a GNU General Public License version 3.0 (or later version)")
    print()

# Lancement du programme
def game():
    start()
    main_menu()

# Menu principal + choix
def main_menu():

    while True:
        print()
        center_print("Press P to PLAY, Q to QUIT, C for the credits")
        center_print(Style.BRIGHT + Fore.YELLOW + ">>> ", -20, False)
        reponse = input().upper()
        print(Style.RESET_ALL, end = "")
        
        if reponse == "P":
            play()
        elif reponse == "KILL":
            quick_quit()
        elif reponse == "Q":
            slow_quit()
        elif reponse == "C":
            credit()

# partie de Mastermind
def play():
    # Code a deviner
    secret_code = []
    try_meter = 0

    for i in range(CODE_SIZE):
        secret_code.append(random.choice(list(COLORS.items())))

    play_menu()

    # Boucle des tours
    while True:

        center_print(Style.BRIGHT + Fore.YELLOW + ">>> ", -21, False)
        query = input().upper()
        print(Style.RESET_ALL, end = "")

        if query == "KILL":
            quick_quit()

        elif query == "GIVE UP":
            center_print(Fore.YELLOW + "Chicken")
            return

        elif query == "HACK":

            str_cheat = ""
            for key, value in secret_code:
                str_cheat = str_cheat + value

            center_print(Fore.RED + "ans:" + str_cheat, -19)
            print()
            continue

        elif query == '':
            continue

        submit = verify_query(query)

        if submit == "erreur":
            center_print(Fore.RED + "Wrong input!", -13)
            print()
            continue

        try_meter += 1

        # Copie du code secret pour pouvoir le manipuler
        code_copy = secret_code.copy()
        submit_copy = submit.copy()
        output = []

        # On verifie d'abord les bonnes couleurs au bon endroit
        for i, (k, v) in enumerate(code_copy):
            if v == submit_copy[i]:
                output.append('!')
                # Valeurs tempon pour ne pas interferer avec d'autre comparaisons
                code_copy[i] = (k, 'X')
                submit_copy[i] = ''

        # On verifie ensuite les bonnes couleurs au mauvais endroit
        for i, digit in enumerate(submit_copy):
            for j, (k, v) in enumerate(code_copy):
                if digit == v:
                    output.append('?')
                    # Valeurs tempon pour ne pas interferer avec d'autre comparaisons
                    code_copy[j] = (k, 'X')
                    submit_copy[i] = ''
                    break

        victory = True
        result_chain = ''
        for i in range(CODE_SIZE):
            if i < len(output):
                result_chain += output[i]

                if output[i] != '!':
                    victory = False
            else:
                # On complete la chaine de resultat avec des espaces pour les mauvaises couleurs
                result_chain += ' '
                victory = False

        attempt = ''
        for color in submit:
            attempt += color

        if (victory):

            center_print(attempt + " was the secret code.")
            center_print(Fore.GREEN + Style.BRIGHT +"Congrats!! " + Style.RESET_ALL +  "It took you " +  str(try_meter) + " step(s).")
            return
        else:
            center_print(attempt + " --> [" + result_chain + "] (?: Color; !: Color + Index)", 3)
            print()

# Entrée dans la partie
def play_menu():

    print()
    center_print(Style.BRIGHT + Fore.GREEN + "Game Start!")
    print()
    center_print("Try a " + str(CODE_SIZE) + " char code [" + COLORS["B"] + ", " + COLORS["G"] + ", " + COLORS["R"] + 
                    ", " + COLORS["Y"] + ", " + COLORS["C"] + ", " + COLORS["P"] + "] or " + Fore.GREEN + "GIVE UP")
                    
# Verification et traduction de l'entrée de l'utilisateur
def verify_query(query):

    attempt = list(query)
    output = []

    if len(attempt) != CODE_SIZE:
        return "erreur"

    for letter in attempt:
        try:
            output.append(COLORS[letter])
        except KeyError:
            return "erreur"

    return output

# Sortie lente du programme
def slow_quit():
    center_print("Unplugging")
    center_print("", -5, False)
    for period in range(5):
        time.sleep(0.2)
        print(". ", end="")

    time.sleep(0.5)

    print()
    center_print(" BRAIN UNPLUGGED!\n")
    time.sleep(0.5)
    center_print("Goodbye.")
    quit()

# Sortie rapide du programme
def quick_quit():
    print()
    center_print(Fore.RED + "Goodbye")
    quit()

# Affichage des crédit
def credit():
    print()
    center_print(Style.BRIGHT + "Developed in 2022 by" + Fore.YELLOW + " StackNoodles™", False)
    print(":\n")
    for title, name in TEAM_NAMES.items():
        center_print(title)
        center_print(name)
        print()
        time.sleep(0.5)
    
    center_print(Style.BRIGHT +Fore.BLACK + "Licensed under GNU General Public License v3.0")
    center_print(Style.BRIGHT +Fore.BLACK + "https://github.com/StackNoodles/Labo1-Mastermind")
    print()
    

    
# Demarrage du programme
if __name__ == '__main__':
    try:
        game()
    except KeyboardInterrupt:
        quick_quit()
    except Exception as e:
        print(Fore.RED)
        print ("    > Fatal Error:")
        print("    > " + str(e))
        quick_quit()