import os
import time
from termcolor import colored

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def adidas_logo():

    print(colored("\n\t\t\t\t\t\t\t\t                      adidas   \n", "white", attrs=["bold"]))

    print(colored("\t\t\t\t\t\t\t\t   ███████             ████             ███████", "white"))
    print(colored("\t\t\t\t\t\t\t\t  ████████████       ████████       ████████████", "white"))
    print(colored("\t\t\t\t\t\t\t\t ███████████████    ██████████    ███████████████", "white"))
    print(colored("\t\t\t\t\t\t\t\t█████████████████  ████████████  █████████████████", "white"))
    print(colored("\t\t\t\t\t\t\t\t █████████████████ ████████████ █████████████████", "white"))
    print()

    print(colored("\t\t\t\t\t\t\t\t    ██████████████████████████████████████████", "white"))
    print()

    print(colored("\t\t\t\t\t\t\t\t       ████████████████████████████████████", "white"))
    print()

    print(colored("\t\t\t\t\t\t\t\t           █████████ ████████ █████████     ", "white"))
    print(colored("\t\t\t\t\t\t\t\t               █████    ██    █████     ", "white"))
    print()
    print(colored("\t\t\t\t\t\t\t\t     █████  ██████  ██ ██████   █████   ██████", "white"))
    print(colored("\t\t\t\t\t\t\t\t    ██   ██ ██   ██ ██ ██   ██ ██   ██ ████", "white"))
    print(colored("\t\t\t\t\t\t\t\t    ███████ ██   ██ ██ ██   ██ ███████    ████", "white"))
    print(colored("\t\t\t\t\t\t\t\t    ██   ██ ██████  ██ ██████  ██   ██ ██████", "white"))
    


clear_screen()
adidas_logo()

