import random
import time
import textwrap
from colorama import init, Fore, Back, Style
init(convert=True)


Color = \
    [Fore.BLUE+"B", #BLUE
     "\033[0;32;10mG\033[0;38;10m", #GREEN
     "\033[0;31;10mR\033[0;38;10m", #RED
     "\033[0;33;10mY\033[0;38;10m", #YELLOW
     "\033[0;36;10mC\033[0;38;10m", #CYAN
     "\033[0;35;10mP\033[0;38;10m"] #PURPLE

set_width=130
def cprint(txt):
    print(txt.center(set_width))

def Start():
    print()
    txt_logo = (Fore.YELLOW+"    ██\      ██\  ██████\   ██████\  ████████\ ████████\ ███████\  ██\      ██\ ██████\ ██\   ██\ ███████\    \n" +
                Fore.YELLOW+"    ███\    ███ |██  __██\ ██  __██\ \__██  __|██  _____|██  __██\ ███\    ███ |\_██  _|███\  ██ |██  __██\   \n" +
                Fore.BLUE+"    ████\  ████ |██ /  ██ |██ /  \__|   ██ |   ██ |      ██ |  ██ |████\  ████ |  ██ |  ████\ ██ |██ |  ██ |  \n" +
                Fore.BLUE+"    ██\██\██ ██ |████████ |\██████\     ██ |   █████\    ███████  |██\██\██ ██ |  ██ |  ██ ██\██ |██ |  ██ | \n" +
                Fore.GREEN+"    ██ \███  ██ |██  __██ | \____██\    ██ |   ██  __|   ██  __██< ██ \███  ██ |  ██ |  ██ \████ |██ |  ██ | \n" +
                Fore.GREEN+"    ██ |\█  /██ |██ |  ██ |██\   ██ |   ██ |   ██ |      ██ |  ██ |██ |\█  /██ |  ██ |  ██ |\███ |██ |  ██ | \n" +
                Fore.RED+"    ██ | \_/ ██ |██ |  ██ |\██████  |   ██ |   ████████\ ██ |  ██ |██ | \_/ ██ |██████\ ██ | \██ |███████  | \n" +
                Fore.RED+"    \__|     \__|\__|  \__| \______/    \__|   \________|\__|  \__|\__|     \__|\______|\__|  \__|\_______/  \n")

    for line in textwrap.wrap(txt_logo, width=118, drop_whitespace=False, break_on_hyphens=True):
        print(line.center(set_width))

    print(Fore.LIGHTWHITE_EX)
    cprint("Developed by" + Fore.YELLOW + " StackNoodles™")
    cprint(Fore.BLACK + "This work is licensed under a GNU General Public License version 3 (or later version)")
    print(Fore.LIGHTWHITE_EX+"\n")


# Lancement du programme
def Game():
    Start()

    MainMenu()

# Menu principal + choix
def MainMenu():

    while True:
        cprint("Press P to PLAY, Q to QUIT, C for the CREDITS \n")
        reponse = input().upper()

        if reponse == "P":
            Partie()
        elif reponse == "Q":
            Quit()
        elif reponse == "C":
            Credit()


# Partie de Mastermind
def Partie():
    # Code a deviner
    code_secret = [Color[random.randint(0,5)],Color[random.randint(0,5)],Color[random.randint(0,5)],Color[random.randint(0,5)]]

    # Entrée dans la partie
    print("Try a 4 char code [" +
          Color[0] + ", " + Color[1] + ", " + Color[2] + ", " + Color[3] + ", " + Color[4] + ", " + Color[5]
          + "] or \033[0;32;10mGIVE UP\033[0;38;10m")

    # Boucle des tours 
    while True:

        query = input()

        if query == "GIVE UP" :
            MainMenu()

        submit = VerifierQuery(query)

        if submit == "erreur" :
            print("Mauvaise Entrée")
        else :
            # Copie du code secret pour pouvoir le manipuler
            copie_code = code_secret.copy()
            sortie = [' ',' ',' ',' ']

            i = 0
            for char in submit :
                # Si le charactere correspond, ecrit '!' dans la sortie et on supprime le char correspondant dans la copie du code secret
                if char == copie_code[i] : 
                    sortie[i] = '!'
                    copie_code[i] = ''

                i += 1

            j = 0
            for char in submit : 
                k = 0
                for code in copie_code :
                    # Si le char correspond a un de ceux du code secret, on écrit '?' dans la sortie et on supprime le char correspondant
                    if char == code and sortie[j] != '!':
                        sortie[j] = '?'
                        copie_code[k] = ''
                        # On ne veut en supprimer qu'un seul
                        break

                    k += 1

                j += 1

            if (sortie[0] + sortie[1] + sortie[2] + sortie[3] == "!!!!"):
                print (submit[0] + submit[1] + submit[2] + submit[3] +" était le code secret, Bravo !!!!")
                MainMenu()
            else :
                print (submit[0] + submit[1] + submit[2] + submit[3] + " --> [" + sortie[0] + sortie[1] + sortie[2] + sortie[3] +
                    "] (! = Bonne Couleur + Bonne Position ; ? = Bonne Couleur)")

# Verification et traduction de l'entrée de l'utilisateur
def VerifierQuery(query):
    essai = list(query)
    sortie = ['','','','']

    if len(essai) == 4:
        i = 0
        for char in essai:
            match char :
                case 'B' :
                    sortie[i] = Color[0]
                case 'G':
                    sortie[i] = Color[1]
                case 'R':
                    sortie[i] = Color[2]
                case 'Y':
                    sortie[i] = Color[3]
                case 'C':
                    sortie[i] = Color[4]
                case 'P':
                    sortie[i] = Color[5]
                case _:
                    return "erreur"
            i += 1
    else :
        return "erreur"

    return sortie

# Fin du programme
def Quit():
    print("Unplugging", end="")
    for period in range(3):
        time.sleep(0.5)
        print(".", end="")
    else:
        time.sleep(0.5)
        print("BRAIN UNPLUGGED!", end="")
        time.sleep(0.5)
        print("\nGoodbye.")
    quit()

def Credit():
    print("PROJECT MANAGER\nMaryse Pilote\n\nLEAD DESIGNER\nYanni Haddar\n\nDEVELOPPERS\nQuentin Gastaldo\nMaryse Pilote\nSam Sebille\n\nCopyright Stack Noodles 2022")

if __name__ == '__main__':
    Game()
