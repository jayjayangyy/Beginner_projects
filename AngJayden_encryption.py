#Ang Jayden
#AngJayden_P1

def main():
    while True:
        plaintext=input("Enter your plaintext:")
        x=len(plaintext)
        ciphertext=""
    
        for a in range(1,x+1):
            y=ord(plaintext[a-1])

            if(y==120):
                z=chr(97)
                ciphertext+=z

            elif(y==121):
                z=chr(98)
                ciphertext+=z

            elif(y==122):
                z=chr(99)
                ciphertext+=z

            else:
                z=chr(y+3)
                ciphertext+=z
                
        print("Your ciphertext is",ciphertext.upper())

        question=input("Do you want to decrypt your ciphertext? ")

        ciphertext.lower()
        decrypt=""
    
        if(question.lower()=="yes"):
            for b in range(1,x+1):
                f=ord(ciphertext[b-1])

                if(f==97):
                    d=chr(120)
                    decrypt+=d

                elif(f==98):
                    d=chr(121)
                    decrypt+=d

                elif(f==99):
                    d=chr(122)
                    decrypt+=d

                else:
                    d=chr(f-3)
                    decrypt+=d

            print("Your decrypted text is",decrypt.lower())
            break

        else:
            break

       
main()
