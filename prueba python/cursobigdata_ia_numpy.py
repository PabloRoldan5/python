import numpy as np

a = np.array([1, 2, 3, 4, 5])

print(a)
print(a[2])

media = a.mean()
print(media)

print(a.sum())


b = np.array([1, 5.6, 'casa'])
b.dtype

b = np.array([1, 5.6, 7])
b.dtype

b.sum
b[2] = 7
print(b)

numeros = np.array([10,20,30,40,50,60,80])
numeros.mean()
numeros.std()
numeros.max()
a1 = np.array([1,1])
a2 = np.array([2,2])
suma = np.add(a1,a2)
suma
suma = a1 + a2
suma
resta = a2 - a1
resta
resta = np.subtract(a2,a1)
resta
multiplicacion = np.multiply(a1,a2)
multiplicacion
a3 = np.array([2,4,6,8])
a3 + 1
np.pi

#ARAYS BIDIMENSIONALES
a = [[11,12,13],[21,22,23],[31,32,33]]
type(a)

array = np.array(a) #CREAMOS ARRAY NUMPY A PARTIR DE LISTA ANIDADA
array.dtype

print("============================")
print(array.size)
print(array.shape)
print(array.ndim)
print(array[1,2])
print(array[1][2])
print(array[0][0:2])
print(array[0,0:2])
print(array[0:2])
print(array[0:2,2])
print("============================")
array2 = np.array([[1,0],[0,1]])
suma = array + array2
array3 = np.array([[2,2],[3,3]])
suma = array2 + array3
suma
multiplicacion = array2 * array3
multiplicacion
4 * array3