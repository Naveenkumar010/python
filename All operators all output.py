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
        if i==0:
            print(add(num1,num2))
            print(sub(num1,num2))
            print(mul(num1,num2))
            print(div(num1,num2))
            print(square(num1,num2))
            print(exp(num1,num2))
