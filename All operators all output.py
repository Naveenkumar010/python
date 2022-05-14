def add(num1,num2):
    return num1+num2
def sub(num1,num):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def square(num1,num2):
    return num1*num1 ,num2*num2
def exp(num1,num2):
    return num1**num2

Ni=int(input("No.of.inputs: "))
for i in range(Ni):
    num1=int(input("Enter the first num : "))
    num2=int(input("enter the second num : "))
    #pass
    op=int(input("The operation to perform: "))
    for i in range(op):
        if i==1:
            print(add(num1,num2))
        elif i==2:
            print(sub(num1,num2))
        elif i==3:
            print(mul(num1,num2))
        elif i==4:
            print(div(num1,num2))
        elif i==5:
            print(square(num1,num2))
        elif i==6:
            print(exp(num1,num2))
