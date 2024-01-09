#Ang Jayden
#AngJayden_Check Code

def main():
    NRIC=input("Enter your NRIC:")
    weight=[2,7,6,5,4,3,2]
    checkdigit=["J","A","B","C","D","E","F","G","H","I","Z"]
           
    if(len(NRIC)!=9):
        print("Your NRIC is not valid.")

    elif(NRIC[0]!="S"):
        print("Your NRIC is not valid.")

    elif(NRIC[-1] not in checkdigit):
        print("Your NRIC is not valid.")

    elif(NRIC[1:8].isdigit()== False):
        print("Your NRIC is not valid.")

    else:
        x=0
        y=0
        z=0

        for i in range(2,9):
            x=int(NRIC[i-1])*int(weight[y])
            y +=1
            z +=x
    
        a=z%11
        check=11-a
        if (check==11):
            if (NRIC[-1]==checkdigit[0]):
                print("Your NRIC is valid.")

            else:
                print("Your NRIC is not valid.")
        
        elif (NRIC[-1]==checkdigit[check]):
            print("Your NRIC is valid.")

        else:
            print("Your NRIC is not valid.")
            
          

main()
