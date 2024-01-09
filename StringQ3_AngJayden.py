#Name: Ang Jayden
#String2 Q3

def main():
    string=input("Enter a word:")
    if(len(string)%2==0):
        x=len(string)//2
        print(string[:x])

    else:
        y=len(string)//2+1
        print(string[:y])

main()

    
