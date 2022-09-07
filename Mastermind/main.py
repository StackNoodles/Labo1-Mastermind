from hashlib import new
import random
from re import sub
import time
import textwrap
import shutil
from colorama import init, Fore, Back, Style
init()


Color = \
    ["\033[0;34;10mB\033[0;38;10m",  # BLUE
     "\033[0;32;10mG\033[0;38;10m",  # GREEN
     "\033[0;31;10mR\033[0;38;10m",  # RED
     "\033[0;33;10mY\033[0;38;10m",  # YELLOW
     "\033[0;36;10mC\033[0;38;10m",  # CYAN
     "\033[0;35;10mP\033[0;38;10m"]  # PURPLE

TAILLE_CODE = 4
NOMBRE_ESSAI = 0

size = shutil.get_terminal_size()
set_width=size.columns
def cprint(txt):
    print(txt.center(set_width))

def Start():
    print(Style.NORMAL)
    txt_logo = (Fore.BLUE+"    ██\      ██\  ██████\   ██████\  ████████\ ████████\ ███████\  ██\      ██\ ██████\ ██\   ██\ ███████\    \n" +
                Fore.BLUE+"    ███\    ███ |██  __██\ ██  __██\ \__██  __|██  _____|██  __██\ ███\    ███ |\_██  _|███\  ██ |██  __██\   \n" +
                Fore.GREEN+"    ████\  ████ |██ /  ██ |██ /  \__|   ██ |   ██ |      ██ |  ██ |████\  ████ |  ██ |  ████\ ██ |██ |  ██ |  \n" +
                Fore.GREEN+"    ██\██\██ ██ |████████ |\██████\     ██ |   █████\    ███████  |██\██\██ ██ |  ██ |  ██ ██\██ |██ |  ██ | \n" +
                Fore.YELLOW+"    ██ \███  ██ |██  __██ | \____██\    ██ |   ██  __|   ██  __██< ██ \███  ██ |  ██ |  ██ \████ |██ |  ██ | \n" +
                Fore.YELLOW+"    ██ |\█  /██ |██ |  ██ |██\   ██ |   ██ |   ██ |      ██ |  ██ |██ |\█  /██ |  ██ |  ██ |\███ |██ |  ██ | \n" +
                Fore.RED+"    ██ | \_/ ██ |██ |  ██ |\██████  |   ██ |   ████████\ ██ |  ██ |██ | \_/ ██ |██████\ ██ | \██ |███████  | \n" +
                Fore.RED+"    \__|     \__|\__|  \__| \______/    \__|   \________|\__|  \__|\__|     \__|\______|\__|  \__|\_______/  \n")

    for line in textwrap.wrap(txt_logo, width=118, drop_whitespace=False):
        print(line.center(set_width))

    print(Style.BRIGHT)
    cprint(Fore.BLACK + "Developed by" + Fore.YELLOW + " StackNoodles™")
    cprint(Fore.BLACK + "This work is licensed under a GNU General Public License version 3 (or later version)")
    print(Style.RESET_ALL)


# Lancement du programme
def Game():
    Start()

    MainMenu()

# Menu principal + choix
def MainMenu():

    while True:
        cprint("Press P to PLAY, Q to QUIT, C for the CREDITS")
        print()
        reponse = input().upper()
        #reponse = input(
        #    "Press P to PLAY, Q to QUIT, C for the CREDITS \n").upper()

        if reponse == "P":
            Partie()
        elif reponse == "Q":
            Quit()
        elif reponse == "C":
            Credit()


# Partie de Mastermind
def Partie():
    # Code a deviner
    code_secret = []

    for i in range(TAILLE_CODE):
        code_secret.append(Color[random.randint(0, 5)])

    # Entrée dans la partie
    print("Try a " + str(TAILLE_CODE) + " char code [" +
          Color[0] + ", " + Color[1] + ", " + Color[2] + ", " +
          Color[3] + ", " + Color[4] + ", " + Color[5]
          + "] or \033[0;32;10mGIVE UP\033[0;38;10m")

    # Boucle des tours
    while True:

        query = input().upper()

        if query == "GIVE UP":
            MainMenu()

        submit = VerifierQuery(query)

        if submit == "erreur":
            print("Mauvaise Entrée")
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
                print(essai + " était le code secret, Bravo !!!! \n" +
                "Vous avez mis " + NOMBRE_ESSAI + " essais.")
                MainMenu()
            else:
                print(
                    essai + " --> [" + chaine + "] (! = Bonne Couleur + Bonne Position ; ? = Bonne Couleur)")

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
    print("Unplugging".center(set_width), end="")
    print()
    print("".center((set_width//2)-(5)), end="")
    for period in range(10):
        time.sleep(0.2)
        print(".", end="")
    else:
        time.sleep(0.5)
        print()
        print("BRAIN UNPLUGGED!".center(set_width), end="")
        time.sleep(0.5)
        print()
        print("Goodbye.".center(set_width))
    quit()


def Credit():
    print("PROJECT MANAGER\nMaryse Pilote\n\nLEAD DESIGNER\nYanni Haddar\n\nDEVELOPPERS\nQuentin Gastaldo\nMaryse Pilote\nSam Sebille\n\nCopyright Stack Noodles 2022")


if __name__ == '__main__':
    try:
        Game()
    except KeyboardInterrupt:
        Quit()
    except Exception:
        print ("Fatal Error")
        Quit()
