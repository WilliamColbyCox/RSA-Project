import random
import math

def main():
    choice = "0"
    keyList = generateKeys()
    publicKeys = (keyList[0], keyList[1])
    privateKeys = (keyList[0], keyList[2])
    print("RSA keys have been generated.")
    while choice != "3":
        print("Please select your user type:")
        print("     1. A public user")
        print("     2. The owner of the keys")
        print("     3. Exit program")
        choice = input("Enter your choice: ")
        if choice == "1":
            publicUser(publicKeys)
        elif choice == "2":
            owner(privateKeys)
        else:
            choice = "3"
    print("Bye for now!")

def generateKeys():
    pDone = False
    qDone = False
    while pDone != True:
        p = random.randint(100000, 1000000)
        for i in range(1, p):
            if pow(i, p-1, p) != 1:
                pDone = False
                break
            else:
                pDone = True
    while qDone != True:
        q = random.randint(100000, 1000000)
        for i in range(1, q):
            if pow(i, q-1, q) != 1:
                qDone = False
                break
            else:
                qDone = True
    phi = (p-1) * (q-1)
    eDone = False
    while eDone != True:
        e = random.randint(1, phi-1)
        if math.gcd(e, phi) == 1:
            eDone = True
    gcdList = extended_gcd(e, phi)
    d = gcdList[0]
    n = p * q
    return [n, e, d]


def extended_gcd(a, b):
    if b == 0:
        return (1, 0, a)
    (x, y, d) = extended_gcd(b, a%b)
    return y, x - a//b*y, d


def publicUser(publicKeys):
    choice = "0"
    while choice != "3":
        print("As a public user, what would you like to do?")
        print("     1. Send an encrypted message")
        print("     2. Authenticate a digital signature")
        print("     3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            inputMessage()
        elif choice == "2":
            AuthSignature()
        else:
            choice = "3"
        
def inputMessage():
    message = input("Enter a message: ")
    encrypt(message)
    print("Message encrypted and sent.")
    
def encrypt(message):
    pass
def AuthSignature():
    pass

def owner(privateKeys):
    print("As the owner of the keys, what would you like to do?")
    print("     1. Decrypt a recieved message")
    print("     2. Digitally sign a message")
    print("     3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        decrypt()
    elif choice == "2":
        sign()
    else:
        choice = "3"

def decrypt():
    pass
def sign():
    pass




main()