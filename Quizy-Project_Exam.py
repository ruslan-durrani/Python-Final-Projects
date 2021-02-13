
def pattern():
    choi = input("Pattern 1,2,3 choose: ")
    if choi =="1":
        for x in range(5,0,-1):
            print()
            for j in range(x,0,-1):
                print(j,end=" ")
    elif choi == "2":
        
        for x in range(1,10):
            print()
            for j in range(9,x+1,-1):
                print(j,end=" ")
    elif choi == "3":
        
        for x in range(8,-1,-2):
            print()
            for k in range(8-x,-1,-2):
                print(k,end= "")
def string():
    string = input("Enter any string: ")
    print("The upper casing is : ",string.upper())
    print("The lower casing is : ",string.lower())
    print("The swap casing is : ",string.swapcase())
def LIST():
    LL = ["Avg Positive","Searching in list","Min Max"]
    for x in range(len(LL)):
        print(str(x+1),"): " ,LL[x])
    Choice = input("select choice: 1/2/3 ")
    if Choice == "1":
        L1 = []
        print("Complete List :")
        for x in range(5):
            L1.append(input(f"Enter number {str(x+1)}th: "))
        S = 0
        count = 0
        for x in L1:
            if int(x) >0:
                count +=1
                S += int(x)
        print("The Average of Positive numbers is : ",round(S/count,3))
    elif Choice == "2":
        L1 = []
        print("Complete List :")
        for x in range(5):
            L1.append(input(f"Enter number {str(x+1)}th : "))
        search = input("Enter data to search in list : ")
        if search in L1:
            print("Data Found: ", search)
        else:
            print("Data not available")
    elif Choice == "3":
        L1 = []
        print("Complete List :")
        for x in range(5):
            L1.append(input(f"Enter number {str(x+1)}th: "))
        print("The max value in list is : ",max(L1))
        print("The min value in list is : ",min(L1))
def question1():
    Lq = ["Factorial","Multiplication table","Even ODD"]
    for x in range(len(Lq)):
        print(str(x+1),"): ",Lq[x])
    Choice = input("Enter choice: 1/2/3 : ")
    if Choice == "1":
        L1 = []
        for x in range(5):
            L1.append(input(f"Enter number {str(x+1)}th: "))
        F = 1
        for x in L1:
            F *= int(x)
        print("The Factorial of numbers is: ",F)
    elif Choice == "2":
        print(format("Multiplication Table",">40s"),"\n")
        print(" \t",end="")
        for x in range(1,11):
            print(format(x,"3d"),end=" ")
        print()
        for x in range(60):
            print("-",end="")
        print()
        for x in range(1,11):
            print(format(x,"2d"),"|","\t",end="")
            for j in range(1,11):
                print(format(j*x,"3d"),end=" ")
            print()

    elif Choice == "3":
        L1 = []
        for x in range(5):
            L1.append(input(f"Enter number {str(x+1)}th: "))
        for x in L1:
            if int(x)%2==0:
                print("Even",format(x,"5d"))
            else:
                print("Odd",format(x,"5d"))

def main():
    while True:
    
        L = ["Fact / Mul / MinMax","List Qs","String Qs","Patterns"]
        for x in range(len(L)):
            print(str(x+1),"): ",L[x])
        select = input("Select Question : 1-2-3-4 ")
        if select == "4":
            pattern()
            print()
        elif select == "3":
            string()
            print()
        elif select == "2":
            LIST()
            print()
        elif select == "1":
            question1()
            print()
        Question = input("Do you want to chek another Question : ").upper()
        if Question == "NO" or Question == "EXIT":
            break
main()

