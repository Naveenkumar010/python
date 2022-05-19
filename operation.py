class gow_down():
    def __init__(self,quantity):
        self.quantity=quantity





class shop(gow_down):

    def __int__(self,products):
        self.products=products
    
    def list_product(self):
        print("Availabe products: ")
        for product in self.products:
            print(product)
    
    def get_product(self,get_product):
        if get_product in self.products:
            print("THe product is avilabe do yo want to buy ")
            self.products.remove(get_product)
        else:
            print("product is insufficent")
    
    

products=['rice','dals','oil','paste','sope','chocolates','candy','coffe powder','tea']
o=shop(products)

msg="""
    1.Display products
    2.get prodect
"""
while True:
    print(msg)
    choice= int(input("Enter ur Choice: "))
    if choice==1:
        o.list_product()
    elif choice==2:
        product=input("enter the name of product: ")
        product=product.lower()
        o.get_product(product)
    elif choice>=3:
        print("Get it in the nxt shop nearby")
    
    else:
        print("Thank You come again")
        quit()