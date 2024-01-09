#Ang Jayden
#function

def CUBE(num):
    "Takes in an integer and return the cubic value."
    return num*num*num

def SUBTRACT(num1,num2):
    "Takes in 2 integers and return the result of the subtraction."
    return num1-num2

def DIVIDE(num3,num4):
    "Takes in 2 integers and return the integer quotient."
    if (num4==0):
        num4=1
    return num3//num4

def main():
    num=int(input("Enter a number to be cubed:"))
    print(CUBE(num))

    num1=int(input("Enter a number for subtraction:"))
    num2=int(input("Enter another number to be subtracted from the previous number:"))
    print(SUBTRACT(num1,num2))

    num3=int(input("Enter a dividend:"))
    num4=int(input("Enter a divisor:"))
    print(DIVIDE(num3,num4))

main()
