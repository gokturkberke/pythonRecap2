import numpy as np

numbers = np.array([1,3,5,6,8,13,25])

result =numbers[3]
print(result) #6
result = numbers[-1]
print(result) #25
result = numbers[1:4]
print(result) #[3 5 6]
result = numbers[::-1] #reverse
print(result) #[25 13 8 6 5 3 1]
#--------------------------------
numbers2 = np.array([[1,3,5],[11,12,13],[20,30,40]])
result = numbers2[0]
print(result) #[1 3 5]
result = numbers2[1][1]
print(result) #12
result= numbers2[0,1]
print(result) #3

result = numbers2[:,1]
print(result) #[ 3 12 30]
result = numbers2[:,0:2]
print(result) #[1 3] [11 12] [20 30]

arr1 = np.arange(0,10)
arr2 = arr1
arr2[0] = 99
print(arr1) #[99  1  2  3  4  5  6  7  8  9]
#iki array aynı bellek alanını paylaşıyor ikisi de degisir
arr2=arr1.copy()
arr2[0]=100 #arr1 değişmez
print(arr1) #[99  1  2  3  4  5  6  7  8  9]
print(arr2) #[100   1   2   3   4   5   6   7   8   9]