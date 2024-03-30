def main():
    name = input("Enter the name ")
    try:
        age = int(input("Enter Age "))
    except:
        print("Invalid age")
        return
    print(age)
    if (age < 18):
        print ("Too Young")
    else:
        newage = age+3
        print (name+"@GMIT.ie", newage)


if __name__ == "__main__":
    main()