#Ang Jayden
#Question 1

def main():
    x=0

    for n in range(1,101):
        if (n%3==0 or n%5==0):
            x+=n

    print("The sum is",x)

main()
