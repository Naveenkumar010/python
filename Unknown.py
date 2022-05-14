def int(x,y):
    for i in x:
        while i>0 and i<=10:
            print(i)
        for j in y:
            while j>0 and j<=10:
                print(j)
        return i*j
    print("mul",i*j)
    print(int(x,y))
