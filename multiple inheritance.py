class Dancer:
    def __init__(self,style):
        self.style=style

    def dance(self):
        print(f'Dancing in {self.style}')

class singer:
    def __init__(self, genre):
        self.genre =genre

    def singer(self):
        print(f'Singer {self.genre} music')

class Artist:
    def __init__(self,Printing_metarial):
        self.printing_metarial=Printing_metarial

    def artist(self):
        print(f'Printing with {self.printing_metarial}')


class SuperHuman(Dancer,singer,Artist):
    def __init__(self,style,genre,Printing_metarial,sport):
        Dancer.__init__(self,style)
        singer.__init__(self,genre)
        Artist.__init__(self,Printing_metarial)
        self.sport = sport

    def play_sport(self):
        print(f'playing {self.sport}')


    def dance(self,compitition):          #over Rrride
        print(f'{self.style} here dance {compitition}')




s =SuperHuman('hihop','classical','acralic', 'cricket')
print(s.style)
print(s.dance('fresher'))
print(s.sport)
s.dance('fresher')
s.play_sport()
print(help(SuperHuman))
