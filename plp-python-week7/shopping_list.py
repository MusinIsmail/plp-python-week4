# shopping_list.py

shopping_list = []

while True:
    choice = input("Enter command (add / remove / show / done): ").strip().lower()
    
    if choice == "add":
        item = input("Enter the item to add: ").strip()
        shopping_list.append(item)
        print(f"'{item}' added to your list.")
    elif choice == "remove":
        item = input("Enter the item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed from your list.")
        else:
            print("That item is not on your list.")
    elif choice == "show":
        print("\n--- Current Shopping List ---")
        if not shopping_list:
            print("Your list is empty.")
        else:
            for item in shopping_list:
                print(f"- {item}")
        print("-----------------------------\n")
    elif choice == "done":
        print("Goodbye! Have a great time shopping.")
        break
    else:
        print("Invalid command. Please choose add, remove, show, or done.")