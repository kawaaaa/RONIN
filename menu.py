from mimetypes import init
import time
import os
from re import A
import sys
from turtle import clear
from click import option
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

roninstr = (f'''                                                                                           
{Fore.BLACK}[          {Fore.RED}RRRRRRRRRRRRRRRRR        OOOOOOOOO     {Fore.MAGENTA}NNNNNNNN        NNNNNNNNIIIIIIIIIINNNNNNNN        NNNNNNNN          {Fore.BLACK}]
{Fore.BLACK}[          {Fore.RED}R::::::::::::::::R     OO:::::::::OO   {Fore.MAGENTA}N:::::::N       N::::::NI::::::::IN:::::::N       N::::::N          {Fore.BLACK}]{Fore.BLACK}
{Fore.BLACK}[          {Fore.RED}R::::::RRRRRR:::::R  OO:::::::::::::OO {Fore.MAGENTA}N::::::::N      N::::::NI::::::::IN::::::::N      N::::::N          {Fore.BLACK}]
{Fore.BLACK}[          {Fore.RED}RR:::::R     R:::::RO:::::::OOO:::::::O{Fore.MAGENTA}N:::::::::N     N::::::NII::::::IIN:::::::::N     N::::::N          {Fore.BLACK}]
{Fore.BLACK}[            {Fore.RED}R::::R     R:::::RO::::::O   O::::::O{Fore.MAGENTA}N::::::::::N    N::::::N  I::::I  N::::::::::N    N::::::N          {Fore.BLACK}]
{Fore.BLACK}[            {Fore.RED}R::::R     R:::::RO:::::O     O:::::O{Fore.MAGENTA}N:::::::::::N   N::::::N  I::::I  N:::::::::::N   N::::::N          {Fore.BLACK}]
{Fore.BLACK}[            {Fore.RED}R::::RRRRRR:::::R O:::::O     O:::::O{Fore.MAGENTA}N:::::::N::::N  N::::::N  I::::I  N:::::::N::::N  N::::::N          {Fore.BLACK}]
{Fore.BLACK}[            {Fore.RED}R:::::::::::::RR  O:::::O     O:::::O{Fore.MAGENTA}N::::::N N::::N N::::::N  I::::I  N::::::N N::::N N::::::N          {Fore.BLACK}]
{Fore.BLACK}[            {Fore.RED}R::::RRRRRR:::::R O:::::O     O:::::O{Fore.MAGENTA}N::::::N  N::::N:::::::N  I::::I  N::::::N  N::::N:::::::N          {Fore.BLACK}]
{Fore.BLACK}[            {Fore.RED}R::::R     R:::::RO:::::O     O:::::O{Fore.MAGENTA}N::::::N   N:::::::::::N  I::::I  N::::::N   N:::::::::::N          {Fore.BLACK}]
{Fore.BLACK}[            {Fore.RED}R::::R     R:::::RO:::::O     O:::::O{Fore.MAGENTA}N::::::N    N::::::::::N  I::::I  N::::::N    N::::::::::N          {Fore.BLACK}]
{Fore.BLACK}[            {Fore.RED}R::::R     R:::::RO::::::O   O::::::O{Fore.MAGENTA}N::::::N     N:::::::::N  I::::I  N::::::N     N:::::::::N          {Fore.BLACK}]
{Fore.BLACK}[          {Fore.RED}RR:::::R     R:::::RO:::::::OOO:::::::O{Fore.MAGENTA}N::::::N      N::::::::NII::::::IIN::::::N      N::::::::N          {Fore.BLACK}]
{Fore.BLACK}[          {Fore.RED}R::::::R     R:::::R OO:::::::::::::OO {Fore.MAGENTA}N::::::N       N:::::::NI::::::::IN::::::N       N:::::::N          {Fore.BLACK}]
{Fore.BLACK}[          {Fore.RED}R::::::R     R:::::R   OO:::::::::OO   {Fore.MAGENTA}N::::::N        N::::::NI::::::::IN::::::N        N::::::N          {Fore.BLACK}]
{Fore.BLACK}[          {Fore.RED}RRRRRRRR     RRRRRRR     OOOOOOOOO     {Fore.MAGENTA}NNNNNNNN         NNNNNNNIIIIIIIIIINNNNNNNN         NNNNNNN          {Fore.BLACK}]
                                                                                   {Fore.RED}[ Created by -kawa#6901 ]''')
roninstr2 = (f'''{Fore.BLACK}[          {Fore.RED}8888888b.   .d88888b.  {Fore.MAGENTA}888b    888 8888888 888b    888 
{Fore.BLACK}[          {Fore.RED}888   Y88b d88P" "Y88b {Fore.MAGENTA}8888b   888   888   8888b   888 
{Fore.BLACK}[          {Fore.RED}888    888 888     888 {Fore.MAGENTA}88888b  888   888   88888b  888 
{Fore.BLACK}[          {Fore.RED}888   d88P 888     888 {Fore.MAGENTA}888Y88b 888   888   888Y88b 888 
{Fore.BLACK}[          {Fore.RED}8888888P"  888     888 {Fore.MAGENTA}888 Y88b888   888   888 Y88b888 
{Fore.BLACK}[          {Fore.RED}888 T88b   888     888 {Fore.MAGENTA}888  Y88888   888   888  Y88888 
{Fore.BLACK}[          {Fore.RED}888  T88b  Y88b. .d88P {Fore.MAGENTA}888   Y8888   888   888   Y8888 
{Fore.BLACK}[          {Fore.RED}888   T88b  "Y88888P"  {Fore.MAGENTA}888    Y888 8888888 888    Y888 
                                      {Fore.RED}- Thank you for using RONIN''')

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()
print(roninstr)

input('Press ENTER to continue...')
cls()
print(roninstr)

def menu():
    print("[1] Info saver")
    print("[2] Info viewer")
    print("[3] Delete all data")
    print(" ")
    print("[0] Exit the program.")

menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        print("     option 1")
        
    elif option == 2:
        print(roninstr)
        
    elif option == 3:
        print("     option 3")
        
    else:
        menu()
        option = int(input('Enter your option: '))

cls()
print(roninstr2)
time.sleep(3)
cls()