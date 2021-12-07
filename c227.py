
print("Welcme to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print("You have chose encryption")
    msg=input("enter your message to encrypt")
    key=int(input("enter the key(1-94)"))
    encryptedtext=""
    for i in range(len(msg)):
        temp=(ord(msg[i])+key)
        if(temp>126):
            temp=temp-127+32

        encryptedtext+=chr(temp)

    print("encrypted:"+encryptedtext)



    


def decryption():
    print("You have chosen decryption")
    print("message can only be upper or lower case alphabet")
    emsg=input("enter encrypted text")
    dkey=int(input("enter the key(1-94)"))
    decryptedtext=""
    for i in range(len(emsg)):
        temp=(ord(emsg[i])-dkey)
        if(temp<32):
            temp=temp+127-32

        decryptedtext+=chr(temp)

    print("decrypted:"+decryptedtext)







    
    

        
if __name__ == "__main__":
    main()
