class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('Rice, Meat')
    
    def exercise(self):
        raise NotImplementedError

class Crickter(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    #override
    def eat(self):
        print('Vegetables')

    def exercise(self):
        print('No need any gym')

    def __add__(self, other):
        return self.age +  other.age
    
    def __mul__(self, other):
        return self.weight *  other.weight
    
    def __gt__(self, other):
        return self.age > other.age
    

sakib = Crickter('Sakib', 38, 68, 91, 'BD')
mushi = Crickter('Mushfiq', 39, 60, 80, 'BD')
# sakib.eat()
# sakib.exercise()

#plus sign overload
print(2+3)
print('Arif' + ' + Sanjida')
print([1,2,3] + [4,5,6])
print(sakib + mushi)
print(sakib * mushi)
print(sakib > mushi)