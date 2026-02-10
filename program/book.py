class Book:
    def __init__(self,book_id,title,author,is_available):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.is_available= is_available
    
    def borrow(self):
        print(f"Borrowing book {self.book_id}...")
        if self.is_available:
            self.is_available = False
            print("Book borrowed successfully...")
        else:
            print("Book not available")


    def return_book(self):
        print(f"Returning book {self.book_id}...")
        if self.is_available:
            print("Book is already in library")
        else:
            print("Book returned successfullly")
            self.is_available=True
        


    def __str__(self):
        status="Available" if self.is_available else "Borrowed"
        return f"{self.book_id} | {self.title}| {self.author} | {status}"
        
        

class Library:
    def __init__(self):
        self.books=[]
    def store(self,books):
        self.books.append(books)
      
    def summary(self):
        total = len(self.books)
        available = sum(1 for book in self.books if book.is_available)
        borrowed = total - available

        print("\nLibrary Summary")
        print("----------------")
        print(f"Total Books: {total}")
        print(f"Available Books: {available}")
        print(f"Borrowed Books: {borrowed}")


        
            

book1=Book("1","The Story Of A Prison","James Watson",True)
book2=Book("2","The Story Of A Hero","James Watson",True)
book3=Book("3","The Story Of A Villain","James Watson",True)
book4=Book("4","The Story Of A Priest","James Watson",True)
book5=Book("5","The Story Of A Vagabond","James Watson",True)
book6=Book("6","The Story Of An Optimistic","James Watson",True)
book7=Book("7","The Story Of A Pessimistic","James Watson",True)
book8=Book("8","The Story Of A Bodyguard","James Watson",True)

library = Library()

library.store(book1)
library.store(book2)
library.store(book3)
library.store(book4)

book1.borrow()
book3.borrow()

print(book1)
print(book2)
print(book3)

library.summary()

book1.return_book()

library.summary()


