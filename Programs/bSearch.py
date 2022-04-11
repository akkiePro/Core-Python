arr = [2, 5 , 31, 42, 65]
# print("before sorting : ")
# print(arr)
size = len(arr)
pos=-1
print("size ",size)
n=3
# for i in range(size-1):
# 	 for j in range(size-1-i):
# 			if (arr[j] > arr[j+1]):
# 					temp = arr[j+1]
# 					arr[j+1] = arr[j]
# 					arr[j] = temp

# print("\n after sorting : ")
# print(arr)
# def ls(arr, n):
# 	for i in range(size):
# 		if arr[i]==n:
# 			globals()["pos"]=i
# 			return True
# 	return False

# if ls(arr, n):
# 	print("found at ",pos+1)
# else:
# 	print("not found")
def bSearch(arr, l, h, n):
	if l<=h:
		middle = (l+h) //2

		if arr[middle] == n:
			return middle
		elif n<arr[middle]:
			return bSearch(arr, l, middle-1, n)
		else:
			return bSearch(arr, middle+1, h, n)
	else:
		return -1

print(bSearch(arr, 0, len(arr), n))