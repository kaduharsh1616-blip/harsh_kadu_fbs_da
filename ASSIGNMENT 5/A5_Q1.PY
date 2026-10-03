#Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate

incorrect_attempts = 0
while incorrect_attempts < 3:
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == "admin" and password == "password123":
        print("Login successful!")
        break
    else:
        incorrect_attempts += 1
        print(f"Incorrect credentials. You have {3 - incorrect_attempts} attempts left.")
else:
    print("Too many incorrect attempts. Program terminated.")