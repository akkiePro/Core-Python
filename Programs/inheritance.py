class GrandParent:
    def sum(self, a, b):
        c=a+b
        return c
    
class Parent(GrandParent):
    a=10
    b=20
    gp = GrandParent()
    print("sum = ", gp.sum(a, b))
    _sum = gp.sum(a, b)
    _average = gp.sum(a, b) / 2
    print(_average)

class child(Parent):
    p = Parent()
    percentage = p._average*100/p._sum
    print("percentage = ",percentage, "%")