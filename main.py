import hashlib

correct_password = hashlib.sha256("Felipe Lorenzo".encode()).hexdigest()

tries = 3

while tries > 0:
    password = input("Password: ")
    hashed =  hashlib.sha256(password.encode()).hexdigest()

    if hashed == correct_password:
        print("Access granted")
        break
    else:
        tries -= 1
        print("Wrong password. Attempts left: ", tries)

if tries == 0:
    print("Account blocked")