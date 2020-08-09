class Cuadratic:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def solve(self):
        if ((self.b)**2 - 4*(self.a)*(self.c)) <= 0:
            print("Don't have solution")
            input()
        else:
            positive = (- (self.b) + ((self.b)**2 - 4*(self.a)*(self.c))**0.5)/(2*(self.a))
            negative = (- (self.b) - ((self.b)**2 - 4*(self.a)*(self.c))**0.5)/(2*(self.a))
            return(negative, positive)
            input()
#If we have the next equation.. y=x**2 - 2*x - 24
''' The coefficients are a=1, b=-2 and c=-24 '''
a = Cuadratic(1, -2, -24)
a.solve() #These are de roots of the cuadratic function
input()


