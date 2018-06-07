userID = None
userPW = None
while True:
    userID = input("Please write your id for register: ")
    userPW = input("Please write your password for register: ")
    if userID != False and userPW != False:
        print("Register succesfully completed! LOL\n"+"*"*30)
        break
    else:
        print("PW or ID shouldn't be empty! Please try again...")
        print("*"*30)

while True:
    print("Welcome to login screen :p\n")
    idCONTROL = input("Please write your id for login: ")
    pwCONTROL = input("Please write your password for login: ")

    if idCONTROL == userID and pwCONTROL == userPW:
        print("Login succesfully! Your id {} and pw {}, welcome!\n".format(userID, userPW))
        print("*"*30)
        break
    else:
        print("Pw/Id is not right, try again! lul")
        print("*"*30)