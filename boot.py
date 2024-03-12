from time import sleep
import os

from variables import dot_sleep, boot_dots, banner

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