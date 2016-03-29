name = input("Enter Name: ")
choice = input("(H)ello" "\n(G)oodbye" "\n(Q)uit")

while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid Choice")
        choice = input("(H)ello" "\n(G)oodbye" "\n(Q)uit")

print("Finished")