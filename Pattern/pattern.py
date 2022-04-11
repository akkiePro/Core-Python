class pattern:
    '''
    *
    **
    ***
    ****
    '''
    def show1(self):
        for i in range(1, 5):
            for j in range(0, i):
                print("*  ", end="")
            print("\n")

    '''
    ****
    ***
    **
    *
    '''
    def show2(self):
        for i in range(4, 0, -1):       # you can also use "reversed(range(<start>, <stop>))"
            for j in range(0, i):       # for example, "reversed(range(4, 0))"
                print("*  ", end="")    # it will iterarte in "4 3 2 1" iteration
            print("\n")

    '''
        *
       **
      ***
     ****
     '''
    def show3(self):
        for i in range(4, 0, -1):
            for j in range(0, i):
                print("   ", end="")
            for k in range(5, i, -1):   
                print("*  ", end="")
            print("\n")
    
    '''
        *
       ***
      *****
     *******  Pyramid
    '''
    def show4(self):
        for i in range(4, 0, -1):
            for j in range(0, i):
                print("   ", end="")
            for k in range(5, i, -1):   
                print("*  ", end="")
            for l in range(4, i, -1):
                print("*  ", end="")
            print("\n")

    '''
        *
       ***
      *****
     *******
     *******
      *****     Diamond
       ***
        *
    '''
    def show5(self):
        for i in range(4, 0, -1):
            for j in range(0, i):
                print("   ", end="")
            for k in range(5, i, -1):   
                print("*  ", end="")
            for l in range(4, i, -1):
                print("*  ", end="")
            print("\n")
        for i in range(1, 5):
            for j in range(0, i):
                print("   ", end="")
            for k in range(5, i, -1):
                print("*  ", end="")
            for k in range(4, i, -1):
                print("*  ", end="")
            print("\n")

    '''
    1
    12
    123
    1234
    '''
    def show6(self):
        for i in range(1, 5):
            for j in range(0, i):
                print(i,"  ", end="")
            print("\n")

    '''
    1
    23
    456
    78910
    '''
    def show7(self):
        num=1
        for i in range(1, 5):
            for j in range(0, i):
                print(num,"  ", end="")
                num += 1
            print("\n")

    '''
    A
    BB
    CCC
    DDDD
    '''
    def show8(self):
        num=65
        for i in range(1, 5):
            for j in range(0, i):
                ch = chr(num)
                print(ch,"  ", end="")
            num += 1
            print("\n")
    
    '''
    A
    BC
    DEF
    GHIJ
    '''
    def show9(self):
        num=65
        for i in range(1, 5):
            for j in range(0, i):
                ch = chr(num)
                print(ch,"  ", end="")
                num += 1
            print("\n")
    
    def show10(self):
        num=97
        for i in range(1, 5):
            for j in range(0, i):
                ch = chr(num)
                print(ch,"  ", end="")
                num += 1
            print("\n")

p1 = pattern()

print("############# pattern 1 ###############")
p1.show1()

print("############# pattern 2 ###############")
p1.show2()

print("############# pattern 3 ###############")
p1.show3()

print("############# pattern 4 ###############")
p1.show4()

print("############# pattern 5 ###############")
p1.show5()

print("############# pattern 6 ###############")
p1.show6()

print("############# pattern 7 ###############")
p1.show7()

print("############# pattern 8 ###############")
p1.show8()

print("############# pattern 9 ###############")
p1.show9()

print("############# pattern 10 ##############")
p1.show10()