import random
path= 'GAMES\\PASS_GENERATOR'
Link = (path + 'PASS_FILE.txt')
password_characters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOASDFGHJKLZXCVBNMP1234567890!@#$%*"
password_length = 8
password_pick = [random.choice(password_characters) for _ in range(password_length)]
password = "".join(password_pick)

use  = input ("Want to store a password or need a password :   ")
if 's' in use:
    Password = input("Your password :   ")
    For = input("For which website or login  site is it for    :   ")
    passfile = open(Link,"a")
    passfile.write(Password + " >>> " +  For + '\n')
    print("You can check the passwords in PASSFILE.txt")
if 'n' in use:
    while True:
        print(password)
        ask = input("Do you want it :   ")
        if ask == 's':
            For = input("For what website or login site :   ")
            passfile = open(Link,"a")
            passfile.write(password + " >>> " +  For + '\n')
            print("You can check the passwords in PASSFILE.txt")
            break
        if ask == 'n' :
            password_pick = [random.choice(password_characters) for _ in range(password_length)]
            password = "".join(password_pick)
            
            



    

