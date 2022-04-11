a = int(input("Enter start point a : "))
d = int(input("Enter difference d : "))
n = int(input("Enter where to stop n : "))
ans=0
def fun2(a,d,n):
	if n==0 or d==0:
		return 0
	else:
		ans = a
		print(ans*ans*ans)
		ans = a+d
		return fun2(ans,d,n-1)
	return ans

fun2(a,d,n)
