import random
import time
import textwrap
import shutil

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


# Centrage du texte pour l 'affichage
def cprint(txt):
    print(txt.center(TERMINAL_WIDTH))

# Affichage du Titre
def start():
    print(Style.NORMAL)
    txt_logo = (Fore.BLUE   + "    ██\      ██\  ██████\   ██████\  ████████\ ████████\ ███████\  ██\      ██\ ██████\ ██\   ██\ ███████\ \n" +
                Fore.BLUE   + "    ███\    ███ |██  __██\ ██  __██\ \__██  __|██  _____|██  __██\ ███\    ███ |\_██  _|███\  ██ |██  __██\ \n" +
                Fore.GREEN  + "    ████\  ████ |██ /  ██ |██ /  \__|   ██ |   ██ |      ██ |  ██ |████\  ████ |  ██ |  ████\ ██ |██ |  ██ |\n" +
                Fore.GREEN  + "    ██\██\██ ██ |████████ |\██████\     ██ |   █████\    ███████  |██\██\██ ██ |  ██ |  ██ ██\██ |██ |  ██ |\n" +
                Fore.YELLOW + "    ██ \███  ██ |██  __██ | \____██\    ██ |   ██  __|   ██  __██< ██ \███  ██ |  ██ |  ██ \████ |██ |  ██ |\n" +
                Fore.YELLOW + "    ██ |\█  /██ |██ |  ██ |██\   ██ |   ██ |   ██ |      ██ |  ██ |██ |\█  /██ |  ██ |  ██ |\███ |██ |  ██ |\n" +
                Fore.RED    + "    ██ | \_/ ██ |██ |  ██ |\██████  |   ██ |   ████████\ ██ |  ██ |██ | \_/ ██ |██████\ ██ | \██ |███████  |\n" +
                Fore.RED    + "    \__|     \__|\__|  \__| \______/    \__|   \________|\__|  \__|\__|     \__|\______|\__|  \__|\_______/\n")

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

    # String contenant l'espace pour centrer'
    global str_buffer
    str_buffer = ""
    for whitespace in range((TERMINAL_WIDTH // 2 - (23))):
        str_buffer = str_buffer + " "

    while True:
        cprint("Press P to PLAY, Q to QUIT, C for the credits")

        reponse = input(str_buffer + ">>> ").upper()

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

        query = input(str_buffer + ">>> ").upper()

        if query == "KILL":
            quick_quit()

        elif query == "GIVE UP":
            cprint(Style.RESET_ALL + Fore.YELLOW + "         Chicken")
            print(Style.RESET_ALL)
            main_menu()

        elif query == "HACK":

            str_cheat = ""
            for key, value in secret_code:
                str_cheat = str_cheat + value

            print(Fore.RED + str_buffer + "ans:" + str_cheat + Fore.YELLOW)
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

            str_winpad = ""
            for whitespace in range((TERMINAL_WIDTH // 2) - 12):
                str_winpad = str_winpad + " "

            print(str_winpad + attempt + " was the secret code.")

            str_triespad = ""
            for whitespace in range((TERMINAL_WIDTH // 2) - 16):
                str_triespad = str_triespad + " "
            print(str_triespad + "Congrats!! It took you " +
                  str(try_meter) + " step(s)." + Style.RESET_ALL)
            print()
            main_menu()
        else:
            str_attempt = ""
            for whitespace in range((TERMINAL_WIDTH // 2) - 19):
                str_attempt = str_attempt + " "
            print(str_attempt + attempt + " --> [" + result_chain + "] (? = Color; ! = Color + Position)" +
                  Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT)
            print()

# Entrée dans la partie
def play_menu():

    print()
    cprint("game started!")

    str_askCOLORS = str_buffer + (Style.RESET_ALL + "Try a " + str(CODE_SIZE) + " char code [" +
                                     COLORS["B"] + ", " + COLORS["G"] + ", " + COLORS["R"] + ", " +
                                     COLORS["Y"] + ", " + COLORS["C"] +
                                     ", " + COLORS["P"]
                                     + "] or " + Fore.GREEN + "GIVE UP" + Fore.YELLOW + Style.BRIGHT)

    print(str_askCOLORS.center(TERMINAL_WIDTH))

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

# Sortie rapide du programme
def quick_quit():
    print(Style.RESET_ALL + Fore.RED)
    print("Goodbye".center(TERMINAL_WIDTH))
    quit()

# Affichage des crédit
def credit():
    for title, name in TEAM_NAMES.items():
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
    except Exception as e:
        print(Style.RESET_ALL + Fore.RED)
        print ("    > Fatal Error:")
        print("    > " + str(e))
        quick_quit()
