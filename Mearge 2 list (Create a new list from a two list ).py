def A(x,y):
    B=[]
    for z in x:
        if z%2==0:
            B.append(z)
    for z in y:
        if z%2!=0:
            B.append(z)
    return B
y= [10, 20, 25, 30, 35]
x= [40, 45, 60, 75, 90]
print("the final list  ",A(x,y))
