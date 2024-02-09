import os
import time

import colorama
from colorama import Fore
from dhooks import Webhook

colorama.init(autoreset=True)


def cls():
    os.system('cls')


red = Fore.RED

erm = """
 █     █░▓█████  ▄▄▄▄    ██░ ██  ▒█████   ▒█████   ██ ▄█▀         
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒          
▒█░ █ ░█ ▒███   ▒██▒ ▄██▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░          
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄          
░░██▒██▓ ░▒████▒░▓█  ▀█▓░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄         
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒         
  ▒ ░ ░   ░ ░  ░▒░▒   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░         
  ░   ░     ░    ░    ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░          
    ░       ░  ░ ░       ░  ░  ░    ░ ░      ░ ░  ░  ░            
                      ░                                           
  ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ 
      ░                 ░  ░       ░          ░      ░  ░   ░
"""

print(red + erm)
print(f"{red}[+] Made by Wojzito")


def send_messages(webhook_url, num_messages, message, webhook_name=None, delay=0):
    hook = Webhook(webhook_url)

    message_counter = 0

    if webhook_name:
        hook.username = webhook_name

    for _ in range(num_messages):
        try:
            hook.send(message)
            message_counter += 1
            cls()
            print(red + erm)
            print(f"{red}[+] Made by Wojzito")
            print(f"{red}[+] Message sent! Total messages sent: {message_counter}")
            time.sleep(delay)

        except Exception as e:
            print(f"{red}[+] Error sending message: {e}")

    print(f"{red}[+] Message sending complete.")
    time.sleep(3)
    cls()
    print(red + erm)
    print(f"{red}[+] Made by Wojzito")


while True:
    webhook_url = input(f"{red}[+] Enter webhook: ")
    number = int(input(f"{red}[+] How many messages?: "))
    message = input(f"{red}[+] Enter message: ")
    delay = input(f"{red}[+] Enter delay: ")

    if delay:
        delay = float(delay)
    else:
        delay = 0

    webhook_name = input(f"{red}[+] Enter webhook name (press Enter to skip): ")

    if webhook_name:
        send_messages(webhook_url, number, message, webhook_name, delay)
    else:
        send_messages(webhook_url, number, message, delay)
