class Robot :
    def __init__(self, name , version ):
        self.name=name
        self.version=version


    def moving_forward(self):
        print(f'{self.name} is moving forward')

    def moving_backward(self):
        print(f'{self.name} is moving backward')

    def moving_right(self):
        print(f'{self.name} is moving right')

    def moving_left(self):
        print(f'{self.name} is moving left')


class HouseRobot(Robot):
    def __init__(self, name , version,area_covered ):    #override
        super().__init__(name, version)
        self.area_covered =area_covered

    def clean(self):
        if self.area_covered >0:
            print(f'{self.name} is cleaning the house');
            self.area_covered -=30
            if self.area_covered < 0 :
                self.area_covered=0
                print(f'{self.name} is cleaning done')
        else:
            print(f'Cannot cleaning !!')

    def set_cover_area(self,area):
        if self.area_covered ==0:
            self.area_covered=area
    @staticmethod
    def stop():
        print(f'Stop this.')

    #override  #polimorfism
    def moving_forward(self):
        print(f'moving housebot class moving')
        super().moving_forward()


hBot = HouseRobot('BOB', 1.1,50)
hBot.moving_forward()
hBot.clean()
hBot.clean()
hBot.clean()
hBot.set_cover_area(30)
hBot.clean()
hBot.clean()
print(help(HouseRobot))
