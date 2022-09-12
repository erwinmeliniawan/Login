import json

print("System Login")
system = input("Login or Register")

if system == "Login":
    username = input("Username : ")
    password = input("Password : ")
    with open('dataLogin.json', 'r') as f:
        readable = f.read()
        lines = readable.splitlines()
        
        username = list(filter(lambda l:l.split(',')[0] == username and l.split(',')[1] == password, lines))
        if username:
            print("Login Succesfull")

        else:
            print("Login Failed")

        f.close()

if system == "Register":
    username = input("Username : ")
    password = input("Password : ")
    password1 = input("Confirm Password : ")

    if(password == password1):
        print("Registration Successfully")
        with open('dataLogin.json','a') as f:
            f.write("\n" + username + "," + password)

    else :
        print("registration Failed")