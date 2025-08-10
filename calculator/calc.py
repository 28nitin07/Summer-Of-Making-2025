num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

def Addition(n1,n2):
    total=n1+n2
    print("The sum of ",n1,"and ",n2,"is: ", total)

def Subtraction(n1,n2):
    total=n1-n2
    print("The difference of ",n1,"and ",n2,"is: ", total)

def Multiplication(n1,n2):
    total=n1*n2
    print("The product of ",n1,"and ",n2,"is: ", total)

def Division(n1,n2):
    total=n1/n2
    print("The quotient of ",n1,"and ",n2,"is: ", total)

def Exponential(n1,n2):
    total=n1**n2
    print("The exponent of ",n1,"and ",n2,"is: ", total)

while True:
    choice=int(input("Enter your choice: \n1) Addition \n2) Subtraction \n3) Multiplication \n4) Division \n5) Exponential \n"))
    if choice==1:
        Addition(num1,num2)
    elif choice==2:
        Subtraction(num1,num2)
    elif choice==3:
        Multiplication(num1,num2)
    elif choice==4:
        Division(num1,num2)
    elif choice==5:
        Exponential(num1,num2)
    else: 
        print("Please enter a valid number.")
    exit=input("Do you want to continue? (y/n)")
    if exit in 'nN':
        break
    