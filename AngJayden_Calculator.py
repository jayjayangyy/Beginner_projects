#Ang Jayden
#AngJayden_Calculator
import tkinter as tk
window = tk.Tk()
def menu():
        "Options for calculator"
        print("Welcome to Jayden's Calculator")
        print("Press 1 for Addition")
        print("Press 2 for Subtraction")
        print("Press 3 for Multiplication")
        print("Press 4 for Division")
        print("Press 5 to Power Off")
        x=input("Enter option:")
        if (x.isdigit()==False):
            x=-500 
        return int(x)

def ADD(NUM1,NUM2):
    "Takes in 2 integers and returns the result of the addition"
    return (int(NUM1)+int(NUM2))

def SUBTRACT(NUM1,NUM2):
    "Takes in 2 integers and returns the result of the subtraction"
    return(int(NUM1)-int(NUM2))

def TIMES(NUM1,NUM2):
    "Takes in 2 integers returns the result of the multiplication"
    return(int(NUM1)*int(NUM2))

def DIVIDE(NUM1,NUM2):
    "Takes in 2 integers returns the result of the division"
    if(int(NUM2)!=0):
        return(int(NUM1)/int(NUM2))

    else:   
        return("Infinity")
      
def main():
        choice=0
        while (choice!=5):
                choice=menu()
        
                if (choice==1):
                    NUM1=input("Enter first operand:")
                    while (NUM1.isdigit()== False):
                            NUM1=input("Invalid integer. Please re-enter the first operand using an integer:\n")
                    
                    NUM2=input("Enter second operand: ")
                    while (NUM2.isdigit()== False):
                            NUM2=input("Invalid integer. Please re-enter the second operand using an integer:\n")
                    
                    print(NUM1,"+",NUM2,"=",ADD(NUM1,NUM2),"\n")

                elif (choice==2):
                    NUM1=input("Enter first operand: ")
                    while (NUM1.isdigit()== False):
                            NUM1=input("Invalid integer. Please re-enter the first operand using an integer:\n")
                    
                    NUM2=input("Enter second operand: ")
                    while (NUM2.isdigit()== False):
                            NUM2=input("Invalid integer. Please re-enter the second operand using an integer:\n")
                    
                    print(NUM1,"-",NUM2,"=",SUBTRACT(NUM1,NUM2),"\n")

                elif (choice==3):
                    NUM1=input("Enter first operand: ")
                    while (NUM1.isdigit()== False):
                            NUM1=input("Invalid integer. Please re-enter the first operand using an integer:\n")
                    
                    NUM2=input("Enter second operand: ")
                    while (NUM2.isdigit()== False):
                            NUM2=input("Invalid integer. Please re-enter the second operand using an integer:\n")

                    print(NUM1,"*",NUM2,"=",TIMES(NUM1,NUM2),"\n")

                elif (choice==4):
                    NUM1=input("Enter first operand: ")
                    while (NUM1.isdigit()== False):
                            NUM1=input("Invalid integer. Please re-enter the first operand using an integer:\n")
                    
                    NUM2=input("Enter second operand: ")
                    while (NUM2.isdigit()== False):
                            NUM2=input("Invalid integer. Please re-enter the second operand using an integer:\n")
                    
                    print(NUM1,"/",NUM2,"=",DIVIDE(NUM1,NUM2),"\n")

                elif (choice==5):
                    print("Bye Bye!")
                    

                else:
                    print("Invalid option. Please re-enter an integer from 1 to 5.\n")


main()




