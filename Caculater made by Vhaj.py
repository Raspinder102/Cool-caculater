# Caculater Made by Vhaj
import os
import platform
from colorama import Fore, Style, init

# Initialize colorama
init()

def clear_screen():
    # Clear the screen based on the operating system
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def display_title():
    print(Fore.CYAN + Style.BRIGHT + "*********************************")
    print(Fore.CYAN + Style.BRIGHT + "*        Made by Vhaj           *")
    print(Fore.CYAN + Style.BRIGHT + "*********************************" + Style.RESET_ALL)

def display_menu():
    print(Fore.YELLOW + Style.BRIGHT + "Select operation:" + Style.RESET_ALL)
    print(Fore.GREEN + "1. Add" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Subtract" + Style.RESET_ALL)
    print(Fore.GREEN + "3. Multiply" + Style.RESET_ALL)
    print(Fore.GREEN + "4. Divide" + Style.RESET_ALL)

def calculator():
    while True:
        clear_screen()
        display_title()
        
        display_menu()
        choice = input(Fore.BLUE + "Enter choice (1/2/3/4): " + Style.RESET_ALL)

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input(Fore.CYAN + "Enter first number: " + Style.RESET_ALL))
                num2 = float(input(Fore.CYAN + "Enter second number: " + Style.RESET_ALL))

                if choice == '1':
                    print(Fore.GREEN + f"{num1} + {num2} = {add(num1, num2)}" + Style.RESET_ALL)

                elif choice == '2':
                    print(Fore.GREEN + f"{num1} - {num2} = {subtract(num1, num2)}" + Style.RESET_ALL)

                elif choice == '3':
                    print(Fore.GREEN + f"{num1} * {num2} = {multiply(num1, num2)}" + Style.RESET_ALL)

                elif choice == '4':
                    result = divide(num1, num2)
                    if isinstance(result, str):
                        print(Fore.RED + result + Style.RESET_ALL)
                    else:
                        print(Fore.GREEN + f"{num1} / {num2} = {result}" + Style.RESET_ALL)

            except ValueError:
                print(Fore.RED + "Invalid input! Please enter numeric values." + Style.RESET_ALL)

            input(Fore.YELLOW + "Press Enter to clear the screen and perform another calculation..." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid choice! Please select a valid option." + Style.RESET_ALL)
            input(Fore.YELLOW + "Press Enter to clear the screen and try again..." + Style.RESET_ALL)

if __name__ == "__main__":
    calculator()
