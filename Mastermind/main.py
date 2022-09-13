from hashlib import new
from itertools import count
import random
from re import sub
import time
import textwrap
import shutil
import string
try :
    from colorama import init, Fore, Back, Style
    init()
except Exception :
    print("""
    ////////////////////////////////////////////////////////////////////////////////
    Il vous faut le module Colorama pour lancer ce programme. (pip install colorama)
    ////////////////////////////////////////////////////////////////////////////////
    """)
    quit()

SIZE = shutil.get_terminal_size()
TERMINAL_WIDTH = SIZE.columns

Colors = {
    "B": "\033[0;34;10mB\033[0;38;10m",  # BLUE
    "G": "\033[0;32;10mG\033[0;38;10m",  # GREEN
    "R": "\033[0;31;10mR\033[0;38;10m",  # RED
    "Y": "\033[0;33;10mY\033[0;38;10m",  # YELLOW
    "C": "\033[0;36;10mC\033[0;38;10m",  # CYAN
    "P": "\033[0;35;10mP\033[0;38;10m"  # PURPLE
}

CODE_SIZE = 4


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
    print("This work is licensed under a GNU General Public License version 3 (or later version)".center(
        TERMINAL_WIDTH))
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
        secret_code.append(random.choice(list(Colors.items())))

    play_menu()

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

            for key, value in secret_code:
                str_cheat = str_cheat + value

            print(Fore.RED + str_cheat + Fore.YELLOW)
            continue

        elif query == '':
            continue

        submit = verify_query(query)

        if submit == "erreur":
            print(Style.RESET_ALL + Fore.RED + "Wrong input ".center(TERMINAL_WIDTH) +
                  Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT)
            continue

        try_meter += 1

        # Copie du code secret pour pouvoir le manipuler
        code_copy = secret_code.copy()
        submit_copy = submit.copy()
        output = []

        for i, (k, v) in enumerate(code_copy):
            if v == submit_copy[i]:
                output.append('!')
                code_copy[i] = (k, 'X')
                submit_copy[i] = ''

        for i, digit in enumerate(submit_copy):
            for j, (k, v) in enumerate(code_copy):
                if digit == v:
                    output.append('?')
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
                result_chain += ' '
                victory = False

        attempt = ''
        for color in submit:
            attempt += color

        if (victory):
            str_winpad = ""
            for whitespace in range((TERMINAL_WIDTH // 2) - 12):
                str_winpad = str_winpad + " "

            print(str_winpad + attempt + " was the secret code.")

            str_triespad = ""
            for whitespace in range((TERMINAL_WIDTH // 2) - 16):
                str_triespad = str_triespad + " "
            print(str_triespad + "Congrats!! It took you " +
                  str(try_meter) + " step(s).")
            print()
            main_menu()
        else:
            str_attempt = ""
            for whitespace in range((TERMINAL_WIDTH // 2) - 19):
                str_attempt = str_attempt + " "
            print(str_attempt + attempt + " --> [" + result_chain + "] (? = Color; ! = Color + Position)" +
                  Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT)
            print()

def play_menu():
    # Entrée dans la partie
    print()
    cprint("game started!")
    str_askcolors = ""
    for whitespace in range((TERMINAL_WIDTH // 2) - 23):
        str_askcolors = str_askcolors + " "

    str_askcolors = str_askcolors + (Style.RESET_ALL + "Try a " + str(CODE_SIZE) + " char code [" +
                                     Colors["B"] + ", " + Colors["G"] + ", " + Colors["R"] + ", " +
                                     Colors["Y"] + ", " + Colors["C"] +
                                     ", " + Colors["P"]
                                     + "] or \033[0;32;10mGIVE UP\033[0;38;10m\033[1m" + Fore.YELLOW + Style.BRIGHT)

    print(str_askcolors.center(TERMINAL_WIDTH))

# Verification et traduction de l'entrée de l'utilisateur
def verify_query(query):

    attempt = list(query)
    output = []

    if len(attempt) != CODE_SIZE:
        return "erreur"

    for letter in attempt:
        try:
            output.append(Colors[letter])
        except KeyError:
            return "erreur"

    return output

# Sorties du programme
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
    credit_names = {
        Fore.BLUE + "PROJECT COORDINATOR" + Fore.BLACK : Fore.BLUE + "Maryse Pilote" + Fore.BLACK,
        Fore.GREEN + "QUALITY CONTROL" + Fore.BLACK : Fore.GREEN + "Sam Sebille" + Fore.BLACK,
        Fore.YELLOW + "LEAD DESIGNER" + Fore.BLACK : Fore.YELLOW + "Yanni Haddar" + Fore.BLACK,
        Fore.RED + "LEAD PROGRAMMER" + Fore.BLACK : Fore.RED + "Quentin Gastaldo" + Fore.BLACK
    }

    for title, name in credit_names.items() :
        print(title.center(TERMINAL_WIDTH))
        print(name.center(TERMINAL_WIDTH))
        print()
        time.sleep(0.5)

    print(Style.RESET_ALL)


# Demarrage du programme
if __name__ == '__main__':
    try:
        game()
    except KeyboardInterrupt:
        quick_quit()
    # except Exception as e:
     #   print(Style.RESET_ALL + Fore.RED)
      #  print ("    > Fatal Error:")
       # print("    > " + str(e))
        # quick_quit()
