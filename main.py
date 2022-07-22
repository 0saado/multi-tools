from tools import passgen
from tools import fakehack
import time
import os
from colorama import Fore as F, init
init(autoreset=True)
os.system('cls')
time.sleep(0.3)
def menu():
    print(f"""
    
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

          """)
    print(f"""{F.WHITE}
          
        Select an option:
          
        [1] Password Generator                                      [2] Generate Fake hack lines
          
          """)
    choice = int(input(">>>>> "))
    
    if choice == 1:
        passgen.menu()
    elif choice == 2:
        fakehack.menu()
        
        
if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        os.system('cls')
        print(f'{F.RED}Quitting...')
        time.sleep(1)
        os.system('cls')        