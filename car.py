class Car():
    def __init__(self,brand):
        self.brand = brand
        self.model = 'xxx'
        self.year = 0
        
    def set_model(self):
        self.model = input('please type in car model   ')

    def set_year(self):
        self.year = input ('please type in car year   ')    

    def print_all(self):
        print(self.brand,self.year,self.model)

car1=Car('Ford')
car1.print_all()
car1.set_year()
car1.set_model()
car1.print_all()