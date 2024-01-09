#Ang Jayden
#Question 4

def main():
    start =0
    end = int(input("Enter the end of range: ")) 

    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num, "EVEN")

        else:
            print(num, "ODD")
    


main() 

