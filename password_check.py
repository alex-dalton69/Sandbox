password = str(input("Password: "))
while len(password) < 8:
    print("Error, password must be a minimum of 8 characters long.")
    password = str(input("Password: "))
if len(password) >= 8:
    print("*" * len(password))
