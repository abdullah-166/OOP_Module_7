class Shopping:
    cart = [] #class attribute
    origin = 'China'

    def __init__(self,name, location) -> None:
        self.name = 'do not go' #instance attribute
        self.location = 'in traffic jam'

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'price of {item} is {price} bdt and remaining {remaining}')

    @staticmethod
    def multiply(a, b):
        result = a * b
        print(result)
    
    @classmethod
    def showoff(self, item):
        print('not to buy here')


north_tower = Shopping('North Tower', 'House Building')
north_tower.purchase('T-shirt',1200, 1500)
Shopping.showoff('nothing!!!')
Shopping.multiply(4,5) #static method

        
