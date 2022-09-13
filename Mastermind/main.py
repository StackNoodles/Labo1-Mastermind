from hashlib import new
from itertools import count
import random
from re import sub
import time
import textwrap
import shutil
import string
from colorama import init, Fore, Back, Style
init()

SIZE = shutil.get_terminal_size()
TERMINAL_WIDTH = SIZE.columns

Color = {
    "B" : "\033[0;34;10mB\033[0;38;10m",  # BLUE
    "G" : "\033[0;32;10mG\033[0;38;10m",  # GREEN
    "R" : "\033[0;31;10mR\033[0;38;10m",  # RED
    "Y" : "\033[0;33;10mY\033[0;38;10m",  # YELLOW
    "C" : "\033[0;36;10mC\033[0;38;10m",  # CYAN
    "P" : "\033[0;35;10mP\033[0;38;10m"  # PURPLE
     }

TAILLE_CODE = 4

def cprint(txt):
    print(txt.center(TERMINAL_WIDTH))

def start():
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
        print(line.center(TERMINAL_WIDTH))

    print(Fore.BLACK + Style.BRIGHT)
    dev_str = "    Developed by" + Fore.YELLOW + " StackNoodles™"
    print(dev_str.center(TERMINAL_WIDTH), end="")
    print(Fore.BLACK)
    print("This work is licensed under a GNU General Public License version 3 (or later version)".center(TERMINAL_WIDTH))
    print(Style.RESET_ALL)


# Lancement du programme
def game():
    start()

    main_menu()

# Menu principal + choix
def main_menu():

    while True:
        cprint("Press P to PLAY, Q to QUIT, C for the creditS")
        str_buffer = ""
        for whitespace in range((TERMINAL_WIDTH // 2 - (23))):
            str_buffer = str_buffer + " "

        str_buffer = str_buffer + ">>> "
        reponse = input(str_buffer).upper()

        if reponse == "P":
            partie()
        elif reponse == "KILL":
            quick_quit()
        elif reponse == "Q":
            slow_quit()
        elif reponse == "C":
            credit()


# partie de Mastermind
def partie():
    # Code a deviner
    code_secret = []
    NOMBRE_ESSAI = 0
    for i in range(TAILLE_CODE):
        code_secret.append(random.choice(list(Color.items())))

    # Entrée dans la partie
    print()
    cprint("game started!")
    str_askcolors = ""
    for whitespace in range((TERMINAL_WIDTH // 2) - 23):
        str_askcolors = str_askcolors + " "

    str_askcolors = str_askcolors + (Style.RESET_ALL + "Try a " + str(TAILLE_CODE) + " char code [" +
          Color["B"] + ", " + Color["G"] + ", " + Color["R"] + ", " +
          Color["Y"] + ", " + Color["C"] + ", " + Color["P"]
          + "] or \033[0;32;10mGIVE UP\033[0;38;10m\033[1m" + Fore.YELLOW + Style.BRIGHT)

    print(str_askcolors.center(TERMINAL_WIDTH))

    # Boucle des tours
    while True:

        str_buffer = ""
        for whitespace in range((TERMINAL_WIDTH // 2) - 23):
            str_buffer = str_buffer + " "
        str_buffer = str_buffer + ">>> "
        query = input(str_buffer).upper()

        if query == "KILL":
            quick_quit()

        elif query == "GIVE UP":
            cprint(Style.RESET_ALL + Fore.YELLOW + "         Chicken")
            print(Style.RESET_ALL)
            main_menu()

        elif query == "HACK":
            str_cheat = ""
            for whitespace in range((TERMINAL_WIDTH // 2) - 23):
                str_cheat = str_cheat + " "

            str_cheat = str_cheat + "ans:"

            for key, value in code_secret:
                str_cheat = str_cheat + value
            
            print(Fore.RED + str_cheat + Fore.YELLOW)
            continue

        elif query == '' :
            continue

           

        submit = verifier_query(query)

        if submit == "erreur":
            print(Style.RESET_ALL + Fore.RED + "Wrong input ".center(TERMINAL_WIDTH) + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT)
            continue

        NOMBRE_ESSAI += 1

        # Copie du code secret pour pouvoir le manipuler
        copie_code = code_secret.copy()
        copie_submit = submit.copy()
        sortie = []

        for i,(k,v) in enumerate(copie_code):
            if v == copie_submit[i]:
                sortie.append('!')
                copie_code[i] = (k, 'X')
                copie_submit[i] = ''
        
        for i, digit in enumerate(copie_submit):
            for j, (k,v) in enumerate(copie_code):
                if digit == v:
                    sortie.append('?')
                    copie_code[j] = (k, 'X')
                    copie_submit[i] = ''
                    break


        victoire = True
        chaine = ''
        for i in range(TAILLE_CODE):
            if i < len(sortie) :
                chaine += sortie[i]

                if sortie[i] != '!' :
                    victoire = False
            else:
                chaine += ' '
                victoire = False

        essai = ''
        for couleur in submit:
            essai += couleur

        if (victoire):
            str_winpad = ""
            for whitespace in range((TERMINAL_WIDTH // 2) - 12):
                str_winpad = str_winpad + " "

            print(str_winpad + essai + " was the secret code.")

            str_triespad = ""
            for whitespace in range((TERMINAL_WIDTH // 2) - 16):
                str_triespad = str_triespad + " "
            print(str_triespad + "Congrats!! It took you " + str(NOMBRE_ESSAI) + " step(s).")
            print()
            main_menu()
        else:
            str_essai = ""
            for whitespace in range((TERMINAL_WIDTH // 2) - 19):
                str_essai = str_essai + " "
            print(str_essai + essai + " --> [" + chaine + "] (? = Color; ! = Color + Position)" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT)
            print()
# Verification et traduction de l'entrée de l'utilisateur


def verifier_query(query):

    essai = list(query)
    sortie = []

    if len(essai) != TAILLE_CODE:
        return "erreur"

    for charactere in essai : 
        try : 
            sortie.append(Color[charactere])
        except KeyError : 
            return "erreur"

    return sortie

# Fin du programme


def slow_quit():
    print("Unplugging".center(TERMINAL_WIDTH))
    print("".center((TERMINAL_WIDTH // 2) - (5)), end="")
    for period in range(5):
        time.sleep(0.2)
        print(". ", end="")

    time.sleep(0.5)
    print()
    print("BRAIN UNPLUGGED!".center(TERMINAL_WIDTH), end="")
    time.sleep(0.5)
    print()
    print(" Goodbye.".center(TERMINAL_WIDTH))

    quit()

def quick_quit():
    print(Style.RESET_ALL + Fore.RED)
    print("Goodbye".center(TERMINAL_WIDTH))
    quit()

def credit():
    print(Fore.BLUE)
    print("PROJECT COORDINATOR".center(TERMINAL_WIDTH), end ="")
    print("Maryse Pilote".center(TERMINAL_WIDTH))
    time.sleep(0.5)
    print(Fore.GREEN)
    print("QUALITY CONTROL".center(TERMINAL_WIDTH), end ="")
    cprint("Sam Sebille")
    time.sleep(0.5)
    print(Fore.YELLOW)
    print("LEAD DESIGNER".center(TERMINAL_WIDTH), end ="")
    cprint("Yanni Haddar")
    time.sleep(0.5)
    print(Fore.RED)
    print("LEAD PROGRAMMER".center(TERMINAL_WIDTH), end ="")
    cprint("Quentin Gastaldo")
    print(Style.RESET_ALL)

if __name__ == '__main__':
    try:
        game()
    except KeyboardInterrupt:
        quick_quit()
    #except Exception as e:
     #   print(Style.RESET_ALL + Fore.RED)
      #  print ("    > Fatal Error:")
       # print("    > " + str(e))
        #quick_quit()
