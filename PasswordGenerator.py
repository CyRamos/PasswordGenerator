import random,string
import prettytable,socket

##########Password generation functions##########
def lowercase(userC=0):
        """Generate a random lowercase password"""
        letters = string.ascii_lowercase
        lowerletters = ''.join(random.choice(letters) for i in range(userC))
        return lowerletters

def withDigits(userC=0):
    """Generate a random lowercase,uppercase and digits password"""
    letters = string.ascii_letters
    digits = string.digits*5
    mix = ''.join(random.choice(letters+digits) for i in range(userC))
    return mix

def punctuation(userC=0):
    """Generate a random lowercase,uppercase, digits and punctuation password"""
    puctutation = string.printable
    puc = ''.join(random.choice(puctutation) for i in range(userC))
    return puc

########## Checking against database if the password is there ##########
def checkMillion(userP):
    file1 = open("D:\CSP\Homeworks\Python Project\million.txt", "r")
    for i in file1:
        i.strip()
        if (userP) == i.strip():
            return userP
    file1.close()

#clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#clientSocket.connect(("127.0.0.1", 5976))

print("\n           Time to bruteforce password space, assuming 10k attempts per second:")
########## Information Table of bruteforce attack ##########
x = prettytable.PrettyTable()
x.field_names = ["Length Characters", "Lowercase", "Uppercase,Lowercase&Digits", "Uppercase,Lowercase,Digits&Puctuation"]
x.add_row(["5", "19 Minutes", "1 Day", "8 Days"])
x.add_row(["6", "8 Hours", "65 Days", "2 Years"])
x.add_row(["7", "9 Days", "11 Years", "200 Years"])
x.add_row(["8", "241 Days", "692 Years", "19,000 Years"])
x.add_row(["9", "17 Years", "42,000 Years", "1.8M Years"])
print(x)

########## User Choose his length & parameters ##########
userParameter = input("Which parameter would you like to use?\n1.Lowercase Only\n2.Upper, Lower & Digits\n3.Upper, Lower, Digits & Punctuation\n\nEnter Your Choice: ")
userInput = userParameter
ifParameterError = userParameter.isdigit()
while True:
    while True:
        if ifParameterError == False:
            userParameter = input("1PLease Enter Parameter From 1-3: ")
            ifParameterError = userParameter.isdigit()
        else:
            userInput = int(userParameter)
            break
    if userInput > 3 or userInput < 1:
        userParameter = int(input("2Please Enter Parameter From 1-3: "))
        continue
    else:
        try:
            userInput < 1 or userInput > 3
        except Exception:
            userParameter = int(input("4Please Enter Parameter From 1-3: "))
        else:
            break
userParameter=int(userParameter)
userCharacters = int(input("How long do you want your password will be? "))
while True:
    if userCharacters > 9:
        userCharacters = int(input("5Please Enter Range From 5-9"))
        continue
    elif userCharacters < 5:
        userCharacters = int(input("6Please Enter Range From 5-9"))
        continue
    else:
        break

########## Checking against the Bruteforce_DB if the pass is there so change it and if not give it to client ##########
while True:
    if userParameter == 1:
        toCheck = lowercase(userCharacters)
        checked = checkMillion(toCheck)
        if toCheck == checked:
            continue
        else:
            print("Your New Password is : ", toCheck)
            break
    if userParameter == 2:
        toCheck = withDigits(userCharacters)
        checked = checkMillion(toCheck)
        if toCheck == checked:
            continue
        else:
            print("Your New Password is : ", toCheck)
            break
    if userParameter == 3:
        toCheck = punctuation(userCharacters)
        checked = checkMillion(toCheck)
        if toCheck == checked:
            continue
        else:
            print("Your New Password is : ", toCheck)
            break
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect(("127.0.0.1", 5976))
clientSocket.send("My name is: ".encode()+socket.gethostname().encode()+"\nMy password is: ".encode()+toCheck.encode())
clientSocket.close()