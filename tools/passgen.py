import random
import os
import time
from colorama import Fore as F, init
from string import ascii_letters as lett, punctuation as pun, digits as dig
import pyperclip

init(autoreset=True)


def gen_pw(length):
    os.system("cls")
    time.sleep(1)
    print("Generating.", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    os.system("cls")
    pw = "".join(random.choice(lett + pun + dig) for _ in range(length))
    print(f"{F.WHITE}Your password is: {F.GREEN}{pw}")
    pyperclip.copy(pw)
    print(f"{F.WHITE}Password copied to clipboard.")


def menu():
    os.system("cls")
    time.sleep(1)
    print(f"{F.GREEN}Password Generator:")
    print("Loading.", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    os.system("cls")
    print(
        f"""
          
    {F.MAGENTA}██████╗  █████╗ ███████╗███████╗{F.WHITE} ██████╗ ███████╗███╗   ██╗
    {F.MAGENTA}██╔══██╗██╔══██╗██╔════╝██╔════╝{F.WHITE}██╔════╝ ██╔════╝████╗  ██║
    {F.MAGENTA}██████╔╝███████║███████╗███████╗{F.WHITE}██║  ███╗█████╗  ██╔██╗ ██║
    {F.MAGENTA}██╔═══╝ ██╔══██║╚════██║╚════██║{F.WHITE}██║   ██║██╔══╝  ██║╚██╗██║
    {F.MAGENTA}██║     ██║  ██║███████║███████║{F.WHITE}╚██████╔╝███████╗██║ ╚████║
    {F.MAGENTA}╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝{F.WHITE} ╚═════╝ ╚══════╝╚═╝  ╚═══╝ 
                    {F.RED}-By Saado | © Soodo Team
                    
        """
    )
    print(
        f""" {F.WHITE}
        Choose an option:
        
        [1] Short Password (8 characters) 
        [2] Long Password (16 characters)
        [3] Custom range password
        
          """
    )

    while True:
        try:
            choice = int(input(f"{F.WHITE}>>>>> "))
        except ValueError:
            print(f"{F.RED}Please enter a number.")
            continue
        if choice not in range(1, 4):
            print(f"{F.RED}Please enter a number between 1 and 3.")
            continue
        break

    if choice == 1:
        gen_pw(8)
    elif choice == 2:
        gen_pw(16)
    elif choice == 3:
        os.system("cls")
        lenght = 0
        while True:
            try:
                length = int(
                    input(f"{F.WHITE}Enter the length of the password: "))
            except ValueError:
                print(f"{F.RED}Please enter a number.")
                continue
            if length not in range(1, 100):
                print(f"{F.RED}Please enter a number between 1 and 100.")
                continue
            break
        gen_pw(lenght)

    print(
        f"""{F.WHITE}
          
    [1] Main Menu
    [2] Password Generator
    [3] Exit
          
          """
    )

    while True:
        try:
            choice = int(input(f"{F.WHITE}>>>>> "))
        except ValueError:
            print(f"{F.RED}Please enter a number.")
            continue
        if choice not in range(1, 4):
            print(f"{F.RED}Please enter a number between 1 and 3.")
            continue
        break

    if choice == 1:
        return
    elif choice == 2:
        menu()
    elif choice == 3:
        exit()


if __name__ == "__main__":
    menu()
