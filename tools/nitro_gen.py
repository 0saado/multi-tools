import random
import requests
import os
import time
from colorama import Fore as F, init
from string import ascii_lowercase as lower, ascii_uppercase as upper

init(autoreset=True)


def gen_code():
    return ''.join(random.choice(lower+upper) for _ in range(16))


def save_code(code):
    with open("nitros.txt", "a") as f:
        f.write(f"https://discord.gift/{code}\n")


def menu():
    os.system("cls")
    time.sleep(1)
    print(f"{F.GREEN}Nitro Gen:")
    print("Loading.", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    os.system("cls")
    print(
        f"""
    
{F.MAGENTA}███╗   ██╗██╗████████╗██████╗  ██████╗     {F.WHITE} ██████╗ ███████╗███╗   ██╗
{F.MAGENTA}████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    {F.WHITE}██╔════╝ ██╔════╝████╗  ██║
{F.MAGENTA}██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║    {F.WHITE}██║  ███╗█████╗  ██╔██╗ ██║
{F.MAGENTA}██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║    {F.WHITE}██║   ██║██╔══╝  ██║╚██╗██║
{F.MAGENTA}██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝    {F.WHITE}╚██████╔╝███████╗██║ ╚████║
{F.MAGENTA}╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝     {F.WHITE} ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                              
                    {F.RED}-By Soerensen | © Soodo Team
                                                    
          """
    )

    print(f"{F.WHITE}How many codes do you want to generate?")
    while True:
        try:
            checks = int(input(f"{F.WHITE}>>>>> "))
        except ValueError:
            print(f"{F.RED}Please enter a number.")
            continue
        if checks < 1:
            print(f"{F.RED}Input must be greater than 0.")
            continue
        break

    valid = 0
    try:
        for checked in range(checks):
            os.system("cls")
            nitrocode = gen_code()

            print(
                f"{F.WHITE}Checking code: {F.MAGENTA}{nitrocode}")
            try:
                r = requests.get(
                    f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitrocode}?with_application=false&with_subscription_plan=true")
            except:
                print(f"{F.RED}Error while checking code.")
                continue

            if r.status_code == 200:
                save_code(nitrocode)
                print(f"{F.GREEN}Found code: {nitrocode}\nSaved to nitros.txt")
                valid += 1
            else:
                print(f"{F.RED}Invalid code.")
            print(
                f"{F.WHITE}Checked: {F.MAGENTA}{checked} {F.WHITE}- Valid: {F.GREEN}{valid}\n")
            time.sleep(random.randrange(3, 10) / 10)

    except KeyboardInterrupt:
        print(f"{F.RED}Stopping Generator.")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        pass

    os.system("cls")

    if valid == 0:
        print(f"{F.WHITE}Done! {F.RED}No valid codes found.")
    else:
        print(f"{F.WHITE}Done! {F.GREEN}{valid} valid codes found!\nCheck {F.MAGENTA}nitros.txt {F.WHITE}for the codes!")
    input("Press enter to exit.")

    os.system("cls")
    time.sleep(0.2)

    print(
        f"""{F.WHITE}
          
    [1] Main Menu
    [2] Nitro Code Generator
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
