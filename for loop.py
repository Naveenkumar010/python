x=int(input("Enter the num to multiply: "))
k=x*2
for i in range (x,-1,-1):
    for j in range(k,0,-1):
        k+=x
        print("*", end=" ")
    print("\t\t") 
       