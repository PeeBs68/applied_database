def main():
    nameStr = "Enter Name: "
    ageInt = "Enter Age: "
    while True:
        display_menu()
        choice = int(input("Choice: "))

        if choice == 3:
            break
        elif choice == 1:
            name = get_name(nameStr)
            print (name.upper())
        elif choice == 2:
            try:
                age = get_age(ageInt)
                print (age+1)
            except:
                print("Invalid age entered")


def display_menu():
    print(" ")
    print("Menu")
    print("====")
    print(("1 - Get Name"))
    print(("2 - Get Age")) 
    print(("3 - Exit"))

def get_name(n):
    name = input(n)
    return name


def get_age(a):
    age = int(input(a))
    return age

if __name__ == "__main__":
    main()