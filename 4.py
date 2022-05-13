def A(x,y):
    print("the txt is ",x)
    B=x[::y]
    return B 
print(A("pynative\r", 2))
print(A("pynative", 4))