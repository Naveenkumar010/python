B=lambda a: 'exists' if a.startswith('p') else 'not exists'
x=str(input("Enter the string: "))
print(B(x))