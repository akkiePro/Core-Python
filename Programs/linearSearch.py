list = [4, 5, 7, 13, 18, 22, 31, 42]
size = len(list)
n=42
def lSearch(list, n):
    for i in range(0, size):
        if i < (size):
            if n == list[i]:
                return i+1

position = lSearch(list, n)
if position == None:
    print("not found")
else:
    print("your element is found at position = ", position)