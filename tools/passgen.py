import main
import random
import os
import time
from colorama import Fore as F, init
from string import ascii_letters as lett, punctuation as pun, digits as dig
init(autoreset=True)
def menu():
    os.system('cls')
    time.sleep(1)
    print(f'{F.GREEN}Password Generator:')
    print('Loading.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    os.system('cls')
    print(f"""
          
    {F.MAGENTA}██████╗  █████╗ ███████╗███████╗{F.WHITE} ██████╗ ███████╗███╗   ██╗
    {F.MAGENTA}██╔══██╗██╔══██╗██╔════╝██╔════╝{F.WHITE}██╔════╝ ██╔════╝████╗  ██║
    {F.MAGENTA}██████╔╝███████║███████╗███████╗{F.WHITE}██║  ███╗█████╗  ██╔██╗ ██║
    {F.MAGENTA}██╔═══╝ ██╔══██║╚════██║╚════██║{F.WHITE}██║   ██║██╔══╝  ██║╚██╗██║
    {F.MAGENTA}██║     ██║  ██║███████║███████║{F.WHITE}╚██████╔╝███████╗██║ ╚████║
    {F.MAGENTA}╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝{F.WHITE} ╚═════╝ ╚══════╝╚═╝  ╚═══╝ 
                    {F.RED}-By Saado | © Soodo Team
                    
        """)
    print(f""" {F.WHITE}
        Choose an option:
        
        [1] Short Password (8 characters) 
        [2] Long Password (16 characters)
        [3] Custom range password
        
          """)
    choice = int(input('>>>>> '))
    if choice == 1:
        short()
    elif choice == 2:
        long()
    elif choice == 3:
        custom()
    print(f'''{F.WHITE}
          
    [1] Main Menu
    [2] Password Generator
    [3] Exit
          
          ''')
    choice = int(input('>>>>> '))
    if choice == 1:
        main.menu()
    elif choice == 2:
        menu()
    elif choice == 3:
        exit()
    
def short():
    os.system('cls')
    print('Generating your password.', end='')
    time.sleep(1)
    password = ''.join(random.sample(lett+dig+pun, 8))
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    os.system('cls')
    print('Your password is:')
    print(f'{F.GREEN}{password}')

def long():
    os.system('cls')
    print('Generating your password.', end='')
    time.sleep(1)
    password = ''.join(random.sample(lett+dig+pun, 16))
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    os.system('cls')
    print('Your password is:')
    print(f'{F.GREEN}{password}')

def custom():
    os.system('cls')
    lenth = int(input('Enter the lenth of the password: '))
    os.system('cls')
    print('Generating your password.', end='')
    time.sleep(1)
    password = ''.join(random.sample(lett+dig+pun, lenth))
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    os.system('cls')
    print('Your password is:')
    print(f'{F.GREEN}{password}')
    
    
if __name__ == "__main__":
    menu()