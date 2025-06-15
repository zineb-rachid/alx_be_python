class Book ():
    def __init__(self,title,author,):
        self.title=title
        self.author=author
        self._is_checked_out=False
    def is_available(self):
     return not self._is_checked_out 
    def check_book_out(self):
        if not self._is_checked_out  : # if not means if false the book isn't cheked
         self._is_checked_out =True
    def return_book(self):
           if self._is_checked_out : # if the book cheked (true) make it not cheked because it got returned
            self._is_checked_out = False 

class Library() :
    def __init__(self,):
     self.__books=[] #private list of books 
    def add_book(self,book):
        self.__books.append(book)
    def check_out_book(self,title):
        for book in self.__books:
           if book.title == title and book.is_available() :
               book.check_book_out()
               break
    def return_book(self,title):
        for book in self.__books:
            if book.title == title and book.is_available():
                book.return_book()
                break
    def list_available_books(self):
        for book in self.__books:
            if book.is_available():
                print(f"{book.title} by {book.author} ")
    

    
                