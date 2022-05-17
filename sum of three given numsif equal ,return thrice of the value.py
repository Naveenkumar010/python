a=int(input("Enter the 1st num: "))
b=int(input("Enter the 2nd num: "))
c=int(input("Enter the 3rd num: "))
def sum():
    if a==b and b==c and c==a:
        x=3*(a+b+c)
        print(x)

    else:
        print(a+b+c)
sum()
