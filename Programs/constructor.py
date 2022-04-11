class constructor:
    def __init__(self, pi):
        self.pi = pi
    
    def area(self, r):
        area = self.pi*r*r
        return area

pi = 3.14
obj = constructor(pi)
radius = 10
ans = obj.area(radius)
print("area = ", ans)