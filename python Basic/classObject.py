class Car:
    def __init__(self,brand,color) :
        self.brand=brand
        self.color=color
    def dis(self):
        print("Brand: ",self.brand)
        print("Color: ",self.color)


obj=Car('BMW','Black')

obj.dis()