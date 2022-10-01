class StoryBook :
    #class variable
    discount = 5
    no_of_book=0
    def __init__(self, name , price , author_name,author_birthday,publishing_year):
        self.name=name
        self.price =price
        self.author_name=author_name
        self.author_birthday =author_birthday
        self.publishing_year=publishing_year
        StoryBook.no_of_book +=1
    #regular_method
    def get_book_info(self):
        print(f'Book name is {self.name} and price is {self.price}')

    def get_author_info(self):
        print(f'this book author name is {self.author_name} and birthday year {self.author_birthday}')

    def apply_discount(self):
        self.price=self.price - self.price * (self.discount/100)
    #class method
    @classmethod
    def new_discount(cls, new_discount):
        cls.discount=new_discount
    @classmethod
    def  construct_from_string(cls,book_str):
        name , price , author_name,author_birthday,publishing_year =book_str.split(',')
        return cls(name , price , author_name,author_birthday,publishing_year)
    #static method
    @staticmethod
    def is_new(publishing_year):
        if(publishing_year>2022):
            print("its a new book")
        else:
            print("its a old book ")





book1=StoryBook('ali babar chollish chor',350, "ali", 1920 ,2001 )
book2=StoryBook('ami topu' , 500, "jafar iqbal" , 1960,2010)

book_str=('amar bondhu rashed, 300, humayun ahmed, 1966,2022')
Dta=StoryBook.construct_from_string(book_str)
print(f'string data is {Dta.name}')
print(f'Here Total Book added {StoryBook.no_of_book}')
book1.get_book_info()
book1.get_author_info()
StoryBook.is_new(book1.publishing_year)
print(f'Before discount price {book1.price} tk')
#
# book1.apply_discount()
# print(f'here is {book1.name} book price after discount is {book1.price} tk')

discount = int(input("how much do you want to discount :"))
book1.new_discount(discount)
book1.apply_discount()
print(f'After discount Your price is {book1.price}')


