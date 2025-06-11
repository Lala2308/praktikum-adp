import os
from termcolor import colored

def clear_screen():
    os.system('cls' )

def pertamina_logo():

    print(colored("\n                                pertamina   \n", "white", attrs=["bold"]))

    print(colored("                           ██████████████████", "red"))
    print(colored("                             ██████████████████", "red"))
    print(colored("                               ██████████████████", "red"))
    print(colored("                                 ██████████████████", "red"))
    print(colored("                                   ██████████████████", "red"))
    print()

    print(colored("              ██████████████████", "blue") + "   " + colored("██████████████████", "green") + "   " + colored("███████  ██████  ██████   ██████   █████   ███     ███  ██  ███   ██   █████", "white"))
    print(colored("            ██████████████████", "blue") + "   " + colored("██████████████████", "green") + "     " + colored("██   ██  ██      ██   ██    ██    ██   ██  ████   ████  ██  ████  ██  ██   ██", "white"))
    print(colored("          ██████████████████", "blue") + "   " + colored("██████████████████", "green") + "       " + colored("███████  █████   ██████     ██    ███████  ██ ██ ██ ██  ██  ██ ██ ██  ███████", "white"))
    print(colored("        ██████████████████", "blue") + "   " + colored("██████████████████", "green") + "         " + colored("██       ██      ██ ██      ██    ██   ██  ██  ███  ██  ██  ██  ████  ██   ██", "white"))
    print(colored("      ██████████████████", "blue") + "   " + colored("██████████████████", "green") + "           " + colored("██       ██████  ██  ███    ██    ██   ██  ██       ██  ██  ██   ███  ██   ██", "white"))
    print(colored("    ██████████████████", "blue"))
    print(colored("  ██████████████████", "blue"))
    print(colored("██████████████████", "blue"))

clear_screen()   
pertamina_logo()
