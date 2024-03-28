# Class inheritance is when we create a class that has certain elemenents from another class
# our classes can inherit from other classes by adding the other class name in parenthesis MyClass(OtherClass):

# Example:
class Car:
    def __init__(self):
        self.model = ''
        self.fuel = ''
        self.price = ''
        self.color = ''

    def moves(self):
        print('moves with wheels')


# that inherits from the Car class


class Tesla(Car):
    def __init__(self):
        # use super to inherit from the Car class
        super().__init__()

    def moves(self):
        # here i am using the method from the Car class and adding some code for this Class.
        super().moves()
        print('and uses Electricity as a fuel!')


t_1 = Tesla()
# here we can use the attributes that are inherited from the Car class
t_1.model = '200s'
t_1.price = 20000
t_1.moves()
