import numpy as np

numbers1 = np.random.randint(1,100,6)
numbers2 = np.random.randint(1,100,6)

print(numbers1)
print(numbers2)

# Add two arrays
print(np.add(numbers1, numbers2))
result = numbers1 + numbers2 #veya

result = numbers1 - numbers2
#boyle butun islemleri yapabiliriz

result = np.sin(numbers1)
result = np.sqrt(numbers1)

multi_numbers1 = numbers1.reshape(2,3)
multi_numbers2 = numbers2.reshape(2,3)
result = numbers1 >= 10
#true false doner her sayi icin
