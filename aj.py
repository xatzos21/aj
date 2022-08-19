import os
import datetime
from colorama import *
from art import *

# initializing colorama
init()

# time variable
now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")

print(Fore.LIGHTCYAN_EX+"")
tprint("AWESOME JOURNAL", font="random")
print(""+Style.RESET_ALL)

# display current journal
new_entry = input("ENTER DIARY ENTRY HERE >>>")

here = os.getcwd().replace("\\","/")

if here.upper() in new_entry.upper():
    print("") 
elif new_entry != "":
    with open("journal.text", "a") as file:
        file.write(now + " " + new_entry + "\n")
else:
    print("AEK")

