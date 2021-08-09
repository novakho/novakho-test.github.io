class Elevator:
    def __init__(self,floor_level):
        self.make = "elevator-company"
        self.floor = floor_level

ele=Elevator(2)
print(ele.make)
print(ele.floor)