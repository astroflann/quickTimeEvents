import time
import keyboard
import random
import colorama
from colorama import Fore
import os
import math
colorama.init(autoreset=True)
def clear():
    os.system('cls')
clear()
keys = ['q', 'e', 'r', 'w', 'a', 's', 'd']
error = input("What would you like the starting difficulty to be: ")
if "." in error:
    error = float(error)
else:
    error = int(error)
neededToWin = 5
counter = 0
failure = False
clear()
def main():
    running = True
    while running:
        key = random.choice(keys)
       
        print(Fore.RED + key)
        time.sleep(error)
        clear()
        print(Fore.YELLOW + key)
        time.sleep(error)
        clear()
        print(Fore.GREEN + key)

        start_time = time.time()
        success = False
        while time.time() - start_time < error:
            if keyboard.is_pressed(key):
                success = True
                counter += 1
                break
            
        if success == True and counter == neededToWin:
            clear()
            if error <= 0.2:
                error = 0.2
                print("You have reached the max difficulty!")
                time.sleep(0.5)
                clear()
            else:
                error -= 0.05
            counter = 0
            print(Fore.LIGHTGREEN_EX + "Successful quick time event!\n difficulty increased! Time to react: ", error)
            time.sleep(0.75)
            clear()
        if success == False or failure == True:
            clear()
            print(Fore.LIGHTRED_EX + "You have failed")
            if failure == True:
                print("You pressed to early!")
            failure = False
            counter = 0
            time.sleep(0.75)
            clear()
        

main()
            
            

