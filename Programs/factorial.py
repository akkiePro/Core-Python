from math import factorial

no = int(input("enter number = "))
def fact(no):
    if no == 1:
        return no
    else:
        return no*fact(no-1)
if no < 1:
    print("please enter valid number...")
else:
    ans = fact(no)
    print(ans)