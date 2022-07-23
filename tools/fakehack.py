import main
import time
import os
import random
from string import ascii_letters as lett, punctuation as pun, digits as dig
from colorama import Fore as F, init
init(autoreset=True)
os.system('cls')
def menu():
    os.system('cls')
    time.sleep(1)
    print(f'{F.GREEN}Fake Hack:')
    print('Loading.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    os.system('cls')
    print(f'''
    
    {F.WHITE}███████╗ █████╗ ██╗  ██╗███████╗    {F.GREEN}██╗  ██╗ █████╗  ██████╗██╗  ██╗
    {F.WHITE}██╔════╝██╔══██╗██║ ██╔╝██╔════╝    {F.GREEN}██║  ██║██╔══██╗██╔════╝██║ ██╔╝
    {F.WHITE}█████╗  ███████║█████╔╝ █████╗      {F.GREEN}███████║███████║██║     █████╔╝ 
    {F.WHITE}██╔══╝  ██╔══██║██╔═██╗ ██╔══╝      {F.GREEN}██╔══██║██╔══██║██║     ██╔═██╗ 
    {F.WHITE}██║     ██║  ██║██║  ██╗███████╗    {F.GREEN}██║  ██║██║  ██║╚██████╗██║  ██╗
    {F.WHITE}╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    {F.GREEN}╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                    {F.RED}-By Saado | © Soodo Team
                                                                    
          ''')

    print(f""" {F.WHITE}
    Choose an option:
    
    [1] Windows Ping command
    [2] Random Characters Generated Lines
    [3] Fake Mass Accounts Hacking Tool
    
        """)
    choice = int(input('>>>>> '))
    if choice == 1:
        ping()
    elif choice == 2:
        gen()
    elif choice == 3:
        accounts()
    
    print(f'''{F.WHITE}
          
    [1] Main Menu
    [2] Fake Hack
    [3] Exit
          
          ''')
    choice = int(input('>>>>> '))
    if choice == 1:
        main.menu()
    elif choice == 2:
        menu()
    elif choice == 3:
        exit()
def ping():
    os.system('cls')
    time.sleep(1)
    os.system('color a')
    time.sleep(1)
    os.system('ping www.google.com')
    os.system('ping www.facebook.com')
    os.system('ping www.youtube.com')

def gen():
    os.system('cls')
    time.sleep(2)
    s = lett + pun + dig
    cases = [1, 2]
    for x in range(1000):
        case = random.choice(cases)
        text = ''.join(random.sample(s, 45))
        if case == 1:
            print(f'{F.GREEN}{text}', end='')
        else:
            print(f'{F.GREEN}{text}')
            time.sleep(0.01)    

def accounts():
    os.system('cls')
    time.sleep(2)
    v = 0
    u = 0
    cases = [1, 2]
    for x in range(500):
        case = random.choice(cases)
        if case == 1:
            v += 1
            print(f'{F.GREEN}Account N°{x} Hacked Successfully.')
            os.system(f'title "Hack Tool v2.1 || Valid: {v} || Unvalid: {u}"')
            time.sleep(0.5)
        else:
            u += 1
            print(f'{F.RED}Account N°{x} Failed to Hack.')
            os.system(f'title "Hack Tool v2.1 || Valid: {v} || Unvalid: {u}"')
            time.sleep(0.5)

if __name__ == "__main__":
    menu()