import numpy as np

python_list = [1, 2, 3, 4, 5, 6]

np_array = np.array(python_list) # Convert python list to numpy array

python_multi = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

np_multi = np_array.reshape(3,2) 
print(np_multi) # Output: [[1, 2], [3, 4], [5, 6]]

print(np_multi.shape) # Output: (3, 2) # (satir, sutun) verir
print(np_multi.ndim) # Output: 2 (kac boyutlu oldugunu verir)
print(np_multi.size) # Output: 6 (eleman sayisini verir)
print(np_multi.dtype) # Output: int32 (veri tipini verir)



