class library:
    def __init__(self,books):
        self.books=books
    def list_books(self):
        print("Avilable Books ")
        for books in self.books:
            print(books)
    def borrow_book(self,borrow_book):
        if borrow_book in self.books:
            print("Get your book ")
            self.books.remove(borrow_book)
        else:
            print("The Book is not Avilable")
    def receive_book(self,receive_book):
        print("THe Book has been Returned")
        self.books.append(receive_book)

books=['c','c++','java','python','dart','sql','artificial intelligent' or 'ai','machine learning' or 'ml','data science','Data Analysis']
o=library(books)
msg="""
    1.Display 
    2.Borrow_book
    3.Return_book
"""
while True:
    print(msg)
    choice=int(input("Enter the choice "))
    if choice == 1 :
        o.list_books()
    elif choice==2:
        book=input("Enter the book name to borrow: ")
        book=book.lower()
        o.borrow_book(book)
    elif choice==3:
        book=input("Enter the book name to return: ")
        book=book.lower()
        o.receive_book(book)
    else:
        print("Thank you come again")
        quit()