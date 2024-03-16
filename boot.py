from time import sleep
import os

boot_dots = 5
dot_sleep = 1

banner = r"""
┌─────────────────────────────────────────────────────────┐
│  ____ _ _                             ____ _      _     │
│ / ___(_) |_ __ ___   ___  _ __ ___   / ___(_)_ __| |___ │
│| |  _| | | '_ ` _ \ / _ \| '__/ _ \ | |  _| | '__| / __|│
│| |_| | | | | | | | | (_) | | |  __/ | |_| | | |  | \__ \│
│ \____|_|_|_| |_| |_|\___/|_|  \___|  \____|_|_|  |_|___/│
└─────────────────────────────────────────────────────────┘"""



def lbl(text, time):
    # Split the text into lines using splitlines()
    lines = text.strip().splitlines()

    # Print each line
    for line in lines:
        print(line)
        sleep(time)

def cbc(text, time):
    # Print each character in the text
    for char in text:
        print(char, end="", flush=True)
        sleep(time)
    print("", flush=True)

def bootscreen(boot_dots):
    print("\nBooting", end="")
    for i in range(1,boot_dots):
        sleep(dot_sleep)
        print(" .", end="", flush=True)
    sleep(dot_sleep)
    print(" .", flush=True)
    sleep(dot_sleep)

def display_banner(banner):
    print(str(banner).strip())

def boot(boot_dots, banner):
    bootscreen(boot_dots)
    os.system('clear')
    lbl(banner, time=0.2)
    cbc("\nPlease wait...", time=0.1)
    sleep(3)

def boot_main():
    boot(boot_dots, banner)