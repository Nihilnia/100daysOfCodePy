# Basic user login controller.

# let's say an user wanna register to our system, 
# and he will login with his username/pass

# and he/she have 3 right for register. 
# When 3 times he/she doing wrong, show an error message.

print("Username and password should be at least 3 char, and maximum 8 char.")
rights = 3
while True:
    if not rights == 0:
        userName = input("Please write your username: ")
        userPass = input("Please write your password: ")
        if userName and userPass:
            if len(userName) >= 3 and len(userName) <= 8:
                if len(userPass) >= 3 and len(userPass) <= 8:
                    print("Register succesfuly.")
                    break
                else:
                    rights -= 1
                    print("Password should be at least 3 char, and maximum 8 char")
            else:
                rights -= 1
                print("Username should be at least 3 char, and maximum 8 char")
        else:
            rights -= 1
            print("Username / Password can't be empty!")
    else:
        print("ERROR: YOU DID WRONG THREE TIMES. TRY AGAIN LATER (CAPSLOCK)")
        break