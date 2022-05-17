list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
list=[]
'''for i in list1:
        if i in list2:
            list.append(i)
        if i not in list2:
            list.append(i)
            list.append(list2)

print(list)
list = [i for i in list1 + list2 if i not in list1 or i not in list2]'''
for i in list1+list2:
    if i not in list1 or i not in list2:
        list.append(i)
print(list)