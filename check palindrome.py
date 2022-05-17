def int(x):
    print("num",x)
    num=x
    y=0
    while x>0:
        A=x%10
        y=(y*10)+A
        x=x//10
    if num==y:
        print("it is palindrome")
    else:
       print("it is not palindrome ")
int(121)
int(2568652)
int(2356)