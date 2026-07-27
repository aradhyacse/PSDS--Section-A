stack = []
while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = int(input("Enter element: "))
        stack.append(item)
        print("Element pushed.")
    elif choice == 2:
        if len(stack) == 0:
            print("Stack Underflow")
        else:
            print("Popped element:", stack.pop())
    elif choice == 3:
        print("Stack:", stack)

    elif choice == 4:
        break
    else:
        print("Invalid choice")