import os
from re import A
import sys
from turtle import clear
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

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()
print(roninstr)

input('Press ENTER to continue...')
cls()
print(roninstr)

print("""           \n\n           [1] Info saver
           [2] Info viewer
           [3] Delete info""")