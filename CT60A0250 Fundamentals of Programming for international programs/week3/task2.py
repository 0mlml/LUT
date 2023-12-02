if input("Do you want to stop the execution of the program (y/Y):\n").lower() == "y":
    print("Bye!")
    exit(0)

user = input("Enter username:\n")
pasw = input("Enter password:\n")

if user == "Mark" and pasw == "drowssap":
    print("User recognized.")
else:
    print("You entered an invalid login name or password.")