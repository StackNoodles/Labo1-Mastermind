import random

Color = \
    ["\033[0;34;10mB\033[0;38;10m", #BLUE
     "\033[0;32;10mG\033[0;38;10m", #GREEN
     "\033[0;31;10mR\033[0;38;10m", #RED
     "\033[0;33;10mY\033[0;38;10m", #YELLOW
     "\033[0;36;10mC\033[0;38;10m", #CYAN
     "\033[0;35;10mP\033[0;38;10m"] #PURPLE

def Start():
    print(
        "██\      ██\  ██████\   ██████\  ████████\ ████████\ ███████\  ██\      ██\ ██████\ ██\   ██\ ███████\ \n" +
        "███\    ███ |██  __██\ ██  __██\ \__██  __|██  _____|██  __██\ ███\    ███ |\_██  _|███\  ██ |██  __██\  \n" +
        "████\  ████ |██ /  ██ |██ /  \__|   ██ |   ██ |      ██ |  ██ |████\  ████ |  ██ |  ████\ ██ |██ |  ██ | \n" +
        "██\██\██ ██ |████████ |\██████\     ██ |   █████\    ███████  |██\██\██ ██ |  ██ |  ██ ██\██ |██ |  ██ | \n" +
        "██ \███  ██ |██  __██ | \____██\    ██ |   ██  __|   ██  __██< ██ \███  ██ |  ██ |  ██ \████ |██ |  ██ | \n" +
        "██ |\█  /██ |██ |  ██ |██\   ██ |   ██ |   ██ |      ██ |  ██ |██ |\█  /██ |  ██ |  ██ |\███ |██ |  ██ | \n" +
        "██ | \_/ ██ |██ |  ██ |\██████  |   ██ |   ████████\ ██ |  ██ |██ | \_/ ██ |██████\ ██ | \██ |███████  | \n" +
        "\__|     \__|\__|  \__| \______/    \__|   \________|\__|  \__|\__|     \__|\______|\__|  \__|\_______/\n\n" +
        "Developed by StackNoodles™ \nThis work is licensed under a GNU General Public License version 3 (or later version)\n\n")



def Game():
    Start()

    while True: # A changer
        MainMenu()

    End()
    return 0


def MainMenu():

    checkrep = False
    while not checkrep:
        reponse = input("Press P to PLAY, Q to QUIT, C for the CREDITS \n").upper()

        if reponse == "P":
            Partie()
            checkrep = True
        elif reponse == "Q":
            End()
            checkrep = True
        elif reponse == "C":
            Credit()
            checkrep = True






def Partie():
    secret_code = [Color[random.randint(0,5)],Color[random.randint(0,5)],Color[random.randint(0,5)],Color[random.randint(0,5)]]

    print("Try a 4 char code [" +
          Color[0] + ", " + Color[1] + ", " + Color[2] + ", " + Color[3] + ", " + Color[4] + ", " + Color[5]
          + "] or \033[0;32;10mGIVE UP\033[0;38;10m")

    while True:
        query = input()
        if query == "GIVE UP" :
            break
        submit = VerifierQuery(query)
        if submit == "erreur" :
            print("Mauvaise Entrée")
        else :

            print("submit: "+ str(submit))
            print("code: " + str(secret_code))

            sortie = ""
            cont = ''
            i = 0
            for char in submit :
                cont = ' '
                if char == secret_code[i] :
                    cont = '!'
                else :
                    for code in secret_code:
                        if char == code:
                            cont = '?'
                sortie = sortie + cont
                i += 1

            if (sortie == "!!!!"):
                print ("Bravo !!!!")
            else :
                print (submit[0] + submit[1] + submit[2] + submit[3] + " --> [" + sortie +
                    "] (! = Bonne Couleur + Bonne Position ; ? = Bonne Couleur)")

    return 0

def VerifierQuery(query):
    print(query)
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


def End():
    return 0


def Credit():
    print("PROJECT MANAGER\nMaryse Pilote\n\nLEAD DESIGNER\nYanni Haddar\n\nDEVELOPPERS\nQuentin Gastaldo\nMaryse Pilote\nSam Sebille\n\nCopyright Stack Noodles 2022")


if __name__ == '__main__':
    Game()
