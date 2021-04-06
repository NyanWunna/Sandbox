def main():

    MINIMUM_LENGTH = 3
    password = input("Enter password: ")
    while True:
        if len(password) >= MINIMUM_LENGTH:
            covered_password="*"*len(password)
            print(f"{covered_password}")
            break
        else:
            print("Invalid Password")
            password = input("Enter password: ")


main()