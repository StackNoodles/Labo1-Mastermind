from hashlib import new
import random
from re import sub
import time
import textwrap
import shutil
#import pandas as pd
import string
from colorama import init, Fore, Back, Style
init()

size = shutil.get_terminal_size()
set_width=size.columns

Color = \
    ["\033[0;34;10mB\033[0;38;10m",  # BLUE
     "\033[0;32;10mG\033[0;38;10m",  # GREEN
     "\033[0;31;10mR\033[0;38;10m",  # RED
     "\033[0;33;10mY\033[0;38;10m",  # YELLOW
     "\033[0;36;10mC\033[0;38;10m",  # CYAN
     "\033[0;35;10mP\033[0;38;10m"]  # PURPLE

TAILLE_CODE = 4

def cprint(txt):
    print(txt.center(set_width))

def Start():
    print(Style.NORMAL)
    txt_logo = (Fore.BLUE+"    ██\      ██\  ██████\   ██████\  ████████\ ████████\ ███████\  ██\      ██\ ██████\ ██\   ██\ ███████\ \n" +
                Fore.BLUE+"    ███\    ███ |██  __██\ ██  __██\ \__██  __|██  _____|██  __██\ ███\    ███ |\_██  _|███\  ██ |██  __██\\\n" +
                Fore.GREEN+"    ████\  ████ |██ /  ██ |██ /  \__|   ██ |   ██ |      ██ |  ██ |████\  ████ |  ██ |  ████\ ██ |██ |  ██ |\n" +
                Fore.GREEN+"    ██\██\██ ██ |████████ |\██████\     ██ |   █████\    ███████  |██\██\██ ██ |  ██ |  ██ ██\██ |██ |  ██ |\n" +
                Fore.YELLOW+"    ██ \███  ██ |██  __██ | \____██\    ██ |   ██  __|   ██  __██< ██ \███  ██ |  ██ |  ██ \████ |██ |  ██ |\n" +
                Fore.YELLOW+"    ██ |\█  /██ |██ |  ██ |██\   ██ |   ██ |   ██ |      ██ |  ██ |██ |\█  /██ |  ██ |  ██ |\███ |██ |  ██ |\n" +
                Fore.RED+"    ██ | \_/ ██ |██ |  ██ |\██████  |   ██ |   ████████\ ██ |  ██ |██ | \_/ ██ |██████\ ██ | \██ |███████  |\n" +
                Fore.RED+"    \__|     \__|\__|  \__| \______/    \__|   \________|\__|  \__|\__|     \__|\______|\__|  \__|\_______/\n")

    for line in textwrap.wrap(txt_logo, width=116, drop_whitespace=False):
        print(line.center(set_width))

    print(Fore.BLACK + Style.BRIGHT)
    dev_str = "    Developed by" + Fore.YELLOW + " StackNoodles™"
    print(dev_str.center(set_width), end="")
    print(Fore.BLACK)
    print("This work is licensed under a GNU General Public License version 3 (or later version)".center(set_width))
    print(Style.RESET_ALL)


# Lancement du programme
def Game():
    Start()

    MainMenu()

# Menu principal + choix
def MainMenu():

    while True:
        cprint("Press P to PLAY, Q to QUIT, C for the CREDITS")
        str_buffer = ""
        for whitespace in range((set_width//2-(23))):
            str_buffer = str_buffer + " "

        str_buffer = str_buffer + ">>> "
        reponse = input(str_buffer).upper()

        if reponse == "P":
            Partie()
        elif reponse == "KILL":
            QuickQuit()
        elif reponse == "Q":
            Quit()
        elif reponse == "C":
            Credit()


# Partie de Mastermind
def Partie():
    # Code a deviner
    code_secret = []
    NOMBRE_ESSAI = 0
    for i in range(TAILLE_CODE):
        code_secret.append(Color[random.randint(0, 5)])

    # Entrée dans la partie
    print()
    cprint("Game Started!")
    str_askcolors = ""
    for whitespace in range((set_width//2)-23):
        str_askcolors = str_askcolors + " "

    str_askcolors = str_askcolors + (Style.RESET_ALL + "Try a " + str(TAILLE_CODE) + " char code [" +
          Color[0] + ", " + Color[1] + ", " + Color[2] + ", " +
          Color[3] + ", " + Color[4] + ", " + Color[5]
          + "] or \033[0;32;10mGIVE UP\033[0;38;10m\033[1m" + Fore.YELLOW + Style.BRIGHT)

    print(str_askcolors.center(set_width))
    # Boucle des tours
    while True:
        str_buffer = ""
        for whitespace in range((set_width // 2) - 23):
            str_buffer = str_buffer + " "
        str_buffer = str_buffer + ">>> "
        query = input(str_buffer).upper()
        if query == "KILL":
            QuickQuit()

        elif query == "GIVE UP":
            cprint(Style.RESET_ALL + Fore.YELLOW + "         Chicken")
            print(Style.RESET_ALL)
            MainMenu()

        elif query == "HACK":
            str_cheat = ""
            for whitespace in range((set_width//2)-23):
                str_cheat = str_cheat + " "

            str_cheat = str_cheat + "ans:"
            for code in code_secret:
                str_cheat = str_cheat + code
            print(Fore.RED + str_cheat)

        submit = VerifierQuery(query)

        if submit == "erreur":
            print(Style.RESET_ALL + Fore.RED + "Wrong input ".center(set_width) + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT)
        else:
            NOMBRE_ESSAI += 1

            # Copie du code secret pour pouvoir le manipuler
            copie_code = code_secret.copy()
            sortie = []

            i = 0
            for i in range(TAILLE_CODE):
                sortie.append(' ')
            s = 0

            i = 0
            for char in submit:
                # Si le charactere correspond, ecrit '!' dans la sortie et on supprime le char correspondant dans la copie du code secret
                if char == copie_code[i]:
                    sortie[s] = '!'
                    s += 1
                    copie_code[i] = ''

                i += 1

            j = 0
            for char in submit:
                k = 0
                for code in copie_code:
                    # Si le char correspond a un de ceux du code secret, on écrit '?' dans la sortie et on supprime le char correspondant
                    if char == code and sortie[j] != '!':
                        sortie[s] = '?'
                        s += 1
                        copie_code[k] = ''
                        # On ne veut en supprimer qu'un seul
                        break
                    k += 1
                j += 1

            victoire = True
            chaine = ''
            for reponse in sortie:
                chaine += reponse
                if reponse != '!':
                    victoire = False

            essai = ''
            for couleur in submit:
                essai += couleur

            if (victoire):
                str_winpad = ""
                for whitespace in range((set_width//2)-12):
                    str_winpad = str_winpad + " "

                print(str_winpad + essai + " was the secret code.")

                str_triespad = ""
                for whitespace in range((set_width//2)-16):
                    str_triespad = str_triespad + " "
                print(str_triespad + "Congrats!! It took you " + str(NOMBRE_ESSAI) + " step(s).")
                print()
                MainMenu()
            else:
                str_essai = ""
                for whitespace in range((set_width//2)-19):
                    str_essai = str_essai + " "
                print(str_essai + essai + " --> [" + chaine + "] (? = Color; ! = Color + Position)" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT)
                print()
# Verification et traduction de l'entrée de l'utilisateur


def VerifierQuery(query):
    essai = list(query)
    sortie = []

    if len(essai) == TAILLE_CODE:
        for i in range(TAILLE_CODE):
            match essai[i]:
                case 'B':
                    sortie.append(Color[0])
                case 'G':
                    sortie.append(Color[1])
                case 'R':
                    sortie.append(Color[2])
                case 'Y':
                    sortie.append(Color[3])
                case 'C':
                    sortie.append(Color[4])
                case 'P':
                    sortie.append(Color[5])
                case _:
                    return "erreur"
    else:
        return "erreur"

    return sortie

# Fin du programme


def Quit():
    print("Unplugging".center(set_width))
    print("".center((set_width//2)-(5   )), end="")
    for period in range(5):
        time.sleep(0.2)
        print(". ", end="")
    else:
        time.sleep(0.5)
        print()
        print("BRAIN UNPLUGGED!".center(set_width), end="")
        time.sleep(0.5)
        print()
        print(" Goodbye.".center(set_width))
    quit()

def QuickQuit():
    print(Style.RESET_ALL + Fore.RED)
    print("Goodbye".center(set_width))
    quit()

def Credit():
    print(Fore.BLUE)
    print("PROJECT COORDINATOR".center(set_width), end = "")
    print(Style.DIM + "Maryse Pilote".center(set_width))
    time.sleep(0.5)
    print(Fore.GREEN)
    print("QUALITY CONTROL".center(set_width), end = "")
    cprint("Sam Sebille")
    time.sleep(0.5)
    print(Fore.YELLOW)
    print("LEAD DESIGNER".center(set_width), end = "")
    cprint("Yanni Haddar")
    time.sleep(0.5)
    print(Fore.RED)
    print("LEAD PROGRAMMER".center(set_width), end = "")
    cprint("Quentin Gastaldo")
    print(Style.RESET_ALL)

if __name__ == '__main__':
    try:
        Game()
    except KeyboardInterrupt:
        QuickQuit()
    except Exception as e:
        print(Style.RESET_ALL + Fore.RED)
        print ("    > Fatal Error:")
        print("    > "+e)
        QuickQuit()
