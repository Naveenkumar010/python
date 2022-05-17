list=[1,5,3,7,9]
list[0],list[-1]=list[-1],list[0]
print (list)



size = len(list)
temp = list[0]
list[0] = list[size - 1]
list[size - 1] = temp

print (list)