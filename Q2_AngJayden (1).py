#Ang Jayden
#test Q2

def main():
    x=str(input("Enter a string:"))
    Letters=0
    Numbers=0
    for n in (x):
        if (n.isdigit()):
            Numbers +=1

        elif (n.isalpha()):
            Letters +=1

    print("Letters:",Letters)
    print("Digits:",Numbers)

main()
          
