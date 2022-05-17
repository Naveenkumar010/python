def check(x):
   # y=int(input("Enter a range "))
    if x in range(10,20):
        print("The num exist with in the given range ")
    else:
        print("the  word doesn't exists")
x=int(input("Enter a num to check "))
check(x)