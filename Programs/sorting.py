list = [5, 13, 4 , 7, 42, 31, 22, 18]
size = len(list)
print(size)
def sort(list, size):
    for j in range(0, size-1):
        for i in range(0, size-1):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return list
print(sort(list, size))