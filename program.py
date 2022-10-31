class Library:
    def __init__(self,list_of_books,library_name):
        self.books=list_of_books
        self.name=library_name
    def display(self):
        for i in self.books:
            print(i,end=" ")
    def landBook(self,b,bName):
        if bookInfo[b] is False:
            print(f"{b} book Succcessfully issued")
            bookInfo.update{b:bname}
        else:
            print(f"{b} has already issued to {bookInfo[b]}")
    def addBook(self,b):
       self.books.append(b)
       print("Thanks for contributing to the library")
    def returnBook(self,b):
        self.books.remove(b)
        print("Thanks for returning Hope you enjoyed reading it")
    
    

books=["Geeta","Ramayan","AI","Physics","Chemistry"]
bookInfo={
    # "Geeta":"",
    # "Ramayan": "",
    # "AI":"",
    # "Physics":"",
    # "Chemistry":""
}

