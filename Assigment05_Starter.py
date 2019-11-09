# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog:
# RRoot,1.1.2030,Created started script
# SQuesada, 11/06/2019, Added functionality to add and remove lists
# Sebastian Quesada,11/06/2019,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {"Task", "Priority"}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Open File
f = open("ToDoList.txt", "w+")
f.write("*** To Do List App *** \n")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # Printing the table
        # Printing the table
        print("Displaying tabulated information:  ")
        print("TASK\tPRIORITY")
        for entry in lstTable:
            Task, Priority = entry
            print(Task, "\t", Priority)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # While loop for entering data
        while True:
            print("Adding Data... [Enter EXIT when complete]")
            print("")
            # ***ITEM INPUT**
            # ***ITEM INPUT**
            Task = input("Please Enter a Task: \n")
            if (Task.lower() == "exit"):
                break
            Priority = int(input("    Enter a Priority: \n"))
            # .lower to be able to user uppercase or lower case
            if (Task.lower() == "exit"):
                # booly2 = False
                # Breaks out of the loop of "exit" is used
                break
            else:
                # Creating a list for the Items
                entry = (Task, Priority)
                lstTable.append(entry)
                #lstTable(reverse=True)
                # Writing to the file
                strData = str(lstTable)
               # f.write(strData)
                # Booly true to exit the loop
                booly = True
        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        rem = input("Remove which task?:  ")
        rem2 = int(input("...with which priority? : "))
        entry = (rem, rem2)
        # print(entry)
        if entry in lstTable:
             lstTable.remove(entry)
             print("TASK\tPRIORITY")
             for entry in lstTable:
                 Task, Priority = entry
                 print(Task, "\t", Priority)
        else:
            print("Hey that's not a task...")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        #closes the document and informs the user
        print("Exiting...")
        f.write("Task\tPRIORITY\n\n")
        f.write(str(entry) + " \n ")
        f.write(str(lstTable))
        f.close()
        print("Data saved.")
        break
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        break  # and Exit the program
f.close()
print ("The End!!")