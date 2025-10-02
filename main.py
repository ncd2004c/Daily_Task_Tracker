#!/usr/bin/env python3
import os
import json

#Clear the console
def clear_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

#Check what choice the user made
def userAction():
    choice = int(input("Enter the action number: "))
    if choice == 1:
        progress()
    elif choice == 2:
        print("Checkoff")
    elif choice == 3:
        addTask()
    elif choice == 4:
        removeTask()
    elif choice == 5:
        clear_console()
        quit()
    else:
        clear_console()
        print("Pick a different option")
        main()

#Show Users their Progress Function
def progress():
    clear_console()
    with open('output.json', 'r') as f:
        printData = json.load(f)
        print(json.dumps(printData, indent=4))
    input("Press Enter to continue!")
    clear_console()
    main()


#Adding Tasks function
def addTask():
    clear_console()
    task = input("What task do you want track: ")
    days = int(input("How many days have you done this task: "))
    streaks = int(input("How many days in a row have you done this task: "))
    existing_data = []
    with open('output.json', 'r') as f:
        existing_data = json.load(f)
    data ={
        "Task": task,"Days Completed": days,"Current Streak": streaks
    }
    existing_data.append(data)
    #print(type(existing_data))
    with open('output.json', 'w') as f:
        json.dump(existing_data, f, indent=4)
    print("Task been Added")
    main()

#Remove Task Function
def removeTask():
    clear_console()
    with open('output.json', 'r') as f:
        printData = json.load(f)
    #print(printData[1])
    printData.pop(1)
    with open('output.json', 'w') as f:
        json.dump(printData, f, indent=4)

#main menu UI
def main():
    print("Welcome to your daily task tracker!")
    print("1: See Current Progress")
    print("2: Check off Task")
    print("3: Add Task")
    print("4: Remove Task")
    print("5: Exit")
    userAction()

#To start code
if __name__ == "__main__":
    main()