def int(list):
    print("the list",list)
    A=list[0]
    B=list[-1]
    while A==B:
        return True
    else:
        return False
x = [10, 20, 30, 40, 10]
print(int(x))
y = [75, 65, 35, 75, 30]
print(int(y))