# class Lyrics:
#     def __init__(self , Name):
#         self.name=Name
#     def fullLyrics(self):
#         for i in range(0,3):
#          print(f'{self.name}, doo doo doo doo doo doo')
#         print(f'{self.name}!')
#
# Lyrics('Baby shark').fullLyrics()
# Lyrics('Mommy shark').fullLyrics()
# Lyrics('Daddy shark').fullLyrics()
# Lyrics('Grandma shark').fullLyrics()
# Lyrics('Grandpa shark').fullLyrics()
# Lyrics("Let's go shark").fullLyrics()
#
# Lst = []
# for i in range(int(input())):
#     name = input()
#     score = float(input())
#     ele = [name,score]
#     Lst.append(ele)
#     Lst.sort(key=float)
# print(Lst)
string = "abracadabra"


string = string[:5] + "k" + string[6:]
print(string)
