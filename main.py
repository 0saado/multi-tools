from tools import passgen, fakehack, nitro_gen
import time
import os
from colorama import Fore as F, init


def menu():
    print(
        f"""

    {F.RED}███████╗ █████╗  █████╗ ██████╗  ██████╗     {F.WHITE}████████╗ ██████╗  ██████╗ ██╗
    {F.RED}██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗    {F.WHITE}╚══██╔══╝██╔═══██╗██╔═══██╗██║
    {F.RED}███████╗███████║███████║██║  ██║██║   ██║    {F.WHITE}   ██║   ██║   ██║██║   ██║██║
    {F.RED}╚════██║██╔══██║██╔══██║██║  ██║██║   ██║    {F.WHITE}   ██║   ██║   ██║██║   ██║██║
    {F.RED}███████║██║  ██║██║  ██║██████╔╝╚██████╔╝    {F.WHITE}   ██║   ╚██████╔╝╚██████╔╝███████╗
    {F.RED}╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝     {F.WHITE}   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
    {F.WHITE},_,_,_,_,_,_,_,_,_,_|{F.RED}______________________________________________________
    {F.WHITE}|#|#|#|#|#|#|#|#|#|#|{F.RED}_____________________________________________________/
    {F.WHITE}'-'-'-'-'-'-'-'-'-'-|{F.RED}----------------------------------------------------'
                        {F.RED}-By Saado | © Soodo Team

          """
    )
    print(
        f"""{F.WHITE}

        Select an option:

        [1] Password Generator                                      [2] Generate Fake hack lines


        [3] Generate Nitro Codes                                    [4] Exit
          """
    )
    while True:
        try:
            choice = int(input(f"{F.WHITE}>>>>> "))
        except ValueError:
            print(f"{F.RED}Please enter a number.")
            continue
        if choice not in range(1, 5):
            print(f"{F.RED}Please enter a number between 1 and 4.")
            continue
        break

    if choice == 1:
        passgen.menu()
    elif choice == 2:
        fakehack.menu()
    elif choice == 3:
        nitro_gen.menu()
    elif choice == 4:
        exit()


if __name__ == "__main__":
    init(autoreset=True)
    os.system("cls")
    time.sleep(0.3)
    try:
        while True:
            menu()
    except KeyboardInterrupt:
        os.system("cls")
        print(f"{F.RED}Quitting...")
        time.sleep(1)
        os.system("cls")
