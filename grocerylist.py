# TASK: Create an interactive grocery list manager.

# Define a function to add an item to the list
def listadder(grocerys):
    # Append the item to the list and return it
    item = input("What would you like to add? Enter the word: ").strip().upper()
    return grocerys.append(item)


# Define a function to remove an item from the list
def listremover(grocerys):
    item = input("What would you like to remove? Enter the word: ").strip().upper()
    if item in grocerys: # If the item exists, remove it
        grocerys.remove(item)
        return grocerys
    if item not in grocerys: # If not, display a message saying the item is not in the list
        print("Theres nothing to remove!")
        



# Define a function to display the grocery list
def listdisplayer(grocerys):
    if len(grocerys) == 0: # If the list is empty, display a message
            print("Your list is empty!")
    else: # If the list is not empty, print all items with numbers
         for x in grocerys:
            numlist = 0
            numlist =+ 1
            print(numlist, x)


# Start with an empty grocery list
grocerys = []
# Use a loop to let the user choose an action:
while True:
    listdisplayer(grocerys)
    choice = input("What would you like to do? ")
# (1) Add an item
    if choice == "1":
        listadder(grocerys)
        continue
# (2) Remove an item
    elif choice == "2":
        listremover(grocerys)
        continue
# (3) View the list
    elif choice == "3":
        listdisplayer(grocerys)
        continue
# (4) Exit the program
    elif choice == "4":
        break
    else:
        print("Enter a option!")
        continue
    break
    
# Call the corresponding function based on user input
# Continue looping until the user chooses to exit