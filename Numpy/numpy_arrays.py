import numpy as np

result = np.arange(1,7) 
print(result) # [1 2 3 4 5 6]
result = np.arange(10,50,2)
result = np.zeros(10) #10 tane 0
result = np.ones(10) #10 tane 1
result = np.linspace(0,100,5) #0 ile 100 arasında 5 tane sayı(0,25,50,75,100)
result = np.random.randint(0,10) #0 ile 10 arasında random sayı
result = np.random.randint(0,20,5) #0 ile 20 arasında 5 tane random sayı

result = np.random.rand(5) #0 ile 1 arasında 5 tane random sayı (ondalikli)

result = np.random.randn(5) #negatif ve pozitif random sayılar
#-------------------------
np_array = np.arange(100)
np_multi = np_array.reshape(10,10) #10x10 lük matris
print(np_multi.sum(axis=1)) #her bir satırın toplamı
print(np_multi.sum(axis=0)) #her bir sütunun toplamı
print(np_multi.max()) #en büyük sayı
print(np_multi.min()) #en küçük sayı
print(np_multi.argmax()) #en büyük sayının indexi
print(np_multi.argmin()) #en küçük sayının indexi
print(np_multi.mean()) #ortalama

#-------------------------
