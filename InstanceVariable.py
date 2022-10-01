class storyBook:
    #class variable
    no_of_book = 0
    discount = 0.5
    def __init__(self, Name , Price,Author_name,Author_born):   # its use like a constructor.
        self.name=Name;
        self.price=Price;
        self.author_name=Author_name;
        self.author_born=Author_born;
        self.Publishing =2022 #set fixed value
        storyBook.no_of_book +=1
    #regular method
    def get_book_info(self):
        print(f'the book name: {self.name}, price {self.price} ')
    def get_author_info(self):
        print(f'the author name : {self.author_name}, born{self.author_born} ')
    def get_discount(self):
        self.price = self.price - self.price * (self.discount/100)

book_1 = storyBook('Hamlet', 300, 'Shakspeare' ,1223)
book2=storyBook('the kite Runner',350 ,'khaled hosseini',1945)

"""
print(book_1.name)
book_1.name='lolipop' #modify data
print(book_1.name)
print(book2.price)
"""
book_1.get_book_info()
book2.get_author_info()
storyBook.get_author_info(book_1)
storyBook.get_book_info(book2)
print(f'Total Book Count {storyBook.no_of_book}')
print(f'Normal Price {book_1.price} tk')
#if we want change here modify discount price
book_1.discount = 5
book_1.get_discount()
print(book_1.price)
# d_price =book_1.get_discount()
# print(f'Discount price : after {storyBook.discount}% discount {book_1.price} tk')


