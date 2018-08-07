### James Elgey
MIN_LENGHT = 5

password = input("Enter a password:")
while len(password) < MIN_LENGHT:
    print("Error, password too short...")
    password = input("Enter a password:")
print("Password accepted")
print("*" * len(password))
