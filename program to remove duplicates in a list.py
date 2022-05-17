list=[2,8,2,8,6,4,3,7,9,3]
a=[]
for i in list:
    if i not in a:
        a.append(i)
print(a)