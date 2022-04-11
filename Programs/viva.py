import math
import datetime
import numpy as np
current_time = datetime.datetime.now()

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
 
B = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40] 
 
C = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 

print ("##################### DATE & TIME ####################")
print ("Time now is : ", end = "") 
print (current_time)
print ("\n")

print ("######################## MEAN ########################")
print("mean of A : ", np.mean(A))
print("mean of B : ", np.mean(B))
print("mean of C : ", np.mean(C))
array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [4, 8, 12, 16, 20, 24, 28, 32, 36, 40], [10, 9, 8, 7,6, 5, 4, 3, 2, 1]])
print("Mean A,B & C: ", np.mean(array1))
print ("\n")


print ("###################### Variance ######################")
print("variance of A : ", np.var(A))
print("variance of B : ", np.var(B))
print("variance of C : ", np.var(C))
print("Variance A,B & C: ", np.var(array1))
print ("\n")


print ("################# Euclidian distance #################")
A = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
B = (4, 8, 12, 16, 20, 24, 28, 32, 36, 40)
C = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(A, B)]))
print("Euclidean distance from A to B: ",distance)
print ("\n")


print ("################# Covariance #######################")
def mean(x):
    return sum(x) / len(x)
def covariance(x, y):
    calc = []
    for i in range(len(x)):
	    xi = x[i] - mean(x)
	    yi = y[i] - mean(y)
	    calc.append(xi * yi)
    return sum(calc) / (len(x) - 1)
print("A & B Covariance:",covariance(A, B))
print("A & C Covariance:",covariance(A, C))