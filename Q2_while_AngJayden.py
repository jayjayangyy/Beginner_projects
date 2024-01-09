#Ang Jayden
#while Q2

def main():
    x=str(input("Enter a string:"))
    
    while (len(x)<9 or x.isalnum()== False or x.isdigit()==True or x.isalpha()==True):
        if (len(x)<9):
            x=str(input("Please re-enter another string with more characters:"))

        elif (x.isalnum()== False):
            x=str(input("Please re-enter another string using only numbers and alphabets:"))

        elif (x.isdigit()==True):
            x=str(input("Please re-enter another string using both numbers and alphabets:"))

        else:
            x=str(input("Please re-enter another string using both numbers and alphabets:"))

    print("String accepted.")

main()
            
