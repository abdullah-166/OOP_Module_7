class User:
    def __init__(self, name, age,money) -> None:
        self._name = name
        self._age = age
        self.__money = money

    @property  #getter any setter readonly attribute 
    def age(self):
        return self._age
    
    @property
    def salary(self):
        return self.__money
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            return 'salary can not be negative'
        self.__money += value


abir = User('Abir', 21, 15000)
# print(abir.__money)
print(abir.age)
print(abir.salary)
abir.salary = 5000
print(abir.salary)
