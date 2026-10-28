chores = []
choice = 0

while choice != 4:
    try:
        choice = int(input("What would you like to do?\n1. Add chore\n2. Check off chore\n3. Display chores\n4. Quit\nOption: "))
    except ValueError:
        print("Not A valid option")
        continue



    if choice == 1:
        #Add
        chore = input("Enter a chore for the to-do list: ")
        chores.append(chore)
    elif choice == 2:
        #Check Off
        full_list = ""
        for i, chore in enumerate(chores):
            full_list += f"{i + 1}: {chore}\n"
        print(full_list)
    elif choice == 3:
        #Display list
        pass
    elif choice == 4:
        #Quit
        print("Ended program!")
    else:
        print("Not a valid option")