from math import sqrt

class Triangle:
    def __init__ (self,a,b):
        self.a = a
        self.b = b
    
    @classmethod
    def random(cls):
        print(cls)

    def get_hypotenuse(self):
        return sqrt(self.a ** 2 + self.b ** 2)

    def get_area(self):
        return self.a * self.b * 0.5
    
