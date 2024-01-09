#Name: Ang Jayden
#String2 Q2

def main():
    string=input("Enter a word:")
    if(len(string)<2):
        print("Empty String")

    else:
        print(string[0:2]+ string[-2:])

main()
