class StoryBook :

    no_of_book=0
    discount=2
    def __init__(self, Name,Price,Author_name,Author_born,Publishing_year):
        self.name = Name
        self.price=Price
        self.author_name=Author_name
        self.author_born=Author_born
        self.publishing_year=Publishing_year
        StoryBook.no_of_book+=1


    def get_book_info(self):
        print(f'Book name Is {self.name} and book price is {self.price}tk')


    def get_author_info(self):
        print(f'author name is {self.author_name} and author birthday year is {self.author_born}')


    def get_discount(self):
        self.price=self.price - self.price * (self.discount/100)

class Library:
      def __init__(self, book_list=None):
        if book_list is None:                   #first of all its a empty . here create automatic list .
            self.book_list=[]
        else :
            self.book_list=book_list

      def getAllBook(self):
          for book in self.book_list:
              print(f'Title : {book.name} , price: {book.price}')
      def addBook(self,book):
          self.book_list.append(book)

      def removeBook(self,book):
          self.book_list.remove(book)





book_1=StoryBook('Ami Topu', 450, "jafar iqbal", 1973 , 2022)
book_2= StoryBook('ali baba chollish chor', 500 ,"humayun ajad", 1968, 2002)

# book_2.get_book_info()
# book_2.get_discount()
# book_2.get_book_info()
# print(f'Here Total Book added {StoryBook.no_of_book}')
Public_library = Library()
Public_library.addBook(book_1)   #here using anothere class object
Public_library.addBook(book_2)    #here using anothere class object
Public_library.getAllBook()
Public_library.removeBook(book_1)
Public_library.getAllBook()
