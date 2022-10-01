class Object_sorting:

    def __init__(self, name ,price):
        self.name=name
        self.price=price

    # def priority_sort(self):
    #     return self.price


def object_print(toy_list):
    for toys in toy_list:
        print(f'{toys.name} : {toys.price}')




toy1=Object_sorting("woody",1000)
toy2=Object_sorting('car',100)
toy3=Object_sorting('logo',50)
toy_list=[toy1,toy2,toy3]

# toy_list.sort(key=Object_sorting.priority_sort ,reverse=True)
# object_print(toy_list)

toy_list.sort(key=lambda x:x.price)
object_print(toy_list)
