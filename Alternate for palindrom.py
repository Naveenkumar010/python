x=input("Check Palindrome Number : ")

if x==x[::-1]:
    print("Yes. Given Number is palindrome number.",x)
else:
    print("No. Given Number is not palindrome number.",x)
