x = int(input("Enter the smaller number: "))
y = int(input("Enter the bigger number: "))

while x > y:
    print("Enter smaller number first, then the bigger number.")
    x = int(input("Enter the smaller number: "))
    y = int(input("Enter the bigger number: "))

choice = input("1.Show the even numbers from x to y""\n2.Show the odd numbers from x to y""\n3.Show the squares from x to y""\n4.Exit the program")

while choice != "4":
    if choice == "1":
        for i in range(x, y+1):
            if i % 2 == 0:
                print(i, end=' ')
        print ()
        choice = input("1.Show the even numbers from x to y""\n2.Show the odd numbers from x to y""\n3.Show the squares from x to y""\n4.Exit the program")

    elif choice == "2":
        for i in range(x, y+1):
            if i % 2 == 1:
                print(i, end=' ')
        print ()
        choice = input("1.Show the even numbers from x to y""\n2.Show the odd numbers from x to y""\n3.Show the squares from x to y""\n4.Exit the program")

    elif choice == "3":
        for i in range(x, y+1):
            print(i*i, end=' ')
        print ()
        choice = input("1.Show the even numbers from x to y""\n2.Show the odd numbers from x to y""\n3.Show the squares from x to y""\n4.Exit the program")

    else:
        print("Invalid choice")
        choice = input("1.Show the even numbers from x to y""\n2.Show the odd numbers from x to y""\n3.Show the squares from x to y""\n4.Exit the program")