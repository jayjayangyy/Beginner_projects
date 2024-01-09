#Ang Jayden
#List2

def main():
    print("List of Subjects")
    Subjects=["English", "Higher Chinese", "Math", "Science"]
    x=len(Subjects)

    for i in range(1,x+1):
        print(i,Subjects[i-1])

    print("There are",x,"subjects altogether.\n")
    # print("")
    
    Subjects.insert(2,"Humanities")
    Subjects.append("Infocomm")
    print(Subjects[1:4])
    print(Subjects[-5:-2],"\n")
    # print("")
    
    Scores=[]
    list1=[66,78,59,89,55,70]
    Scores.extend(list1)
   
    y=len(Scores)
    z=len(Subjects)

    print("Number of elements in subjects =",z)
    print("Number of elements in scores =",y)
    
main()
