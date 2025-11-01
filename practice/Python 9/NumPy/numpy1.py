import numpy as np

a = np.int8(25)
print(a)
#25

print(type(a))
# <class 'numpy.int8'>

"""iinfo"""
# Можно применить к самому
# названию типа данных
np.iinfo(np.int8)
# iinfo(min=-128, max=127, dtype=int8)

# Можно применить к существующему
# конкретному объекту
np.iinfo(a)
# iinfo(min=-128, max=127, dtype=int8)

"""беззнаковые целые числа"""
b = np.uint8(124)
print(b)
# 124
print(type(b))
# <class 'numpy.uint8'>
np.iinfo(b)
# iinfo(min=0, max=255, dtype=uint8)

"""Несколько замечаний о приведении типов"""
a = np.int32(1000)
print(a)
# 1000
print(type(a))
# <class 'numpy.int32'>
a = 2056
print(a)
# 2056
print(type(a))
# <class 'int'>

a = np.int32(1000)
b = a + 25
print(b)
# 1025
print(type(b))
# <class 'numpy.int64'>

#берется всегда старший тип
a = np.int32(1000)
b = np.int8(25)
c = a + b
print(c)
# 1025
print(type(c))
# <class 'numpy.int32'>

"""Типы данных с плавающей точкой в NumPy"""
print(np.finfo(np.float16))
# finfo(resolution=0.001, min=-6.55040e+04, max=6.55040e+04, dtype=float16)
print(np.finfo(np.float32))
# finfo(resolution=1e-06, min=-3.4028235e+38, max=3.4028235e+38, dtype=float32)
print   (np.finfo(np.float64))
# finfo(resolution=1e-15, min=-1.7976931348623157e+308, max=1.7976931348623157e+308, dtype=float64)
np.finfo(np.float64)
# finfo(resolution=1e-18, min=-1.189731495357231765e+4932, max=1.189731495357231765e+4932, dtype=float128)

print(np.float16(4.12))
# 4.12
print(np.float16(4.13))
# 4.13
print(np.float16(4.123))
# 4.12
print(np.float16(4.124))
# 4.125
print(np.float16(4.125))
# 4.125

"""Дополнительные типы данных в NumPy"""
print(np.sctypeDict)
print(len(np.sctypeDict))
# 158, но может быть 135 или 139

print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')

a = True
print(type(a))
# <class 'bool'>
a = np.bool(a)
print(type(a))
# <class 'bool'>
a = np.bool_(a)
print(type(a))
# <class 'numpy.bool_'>
 
# Значения равны
print(np.bool(True) == np.bool_(True))
# True
# А типы — нет:
print(type(np.bool(True)) == type(np.bool_(True)))
# False

a = "Hello world!"
print(type(a))
# <class 'str'>
###a = np.str(a)
print(type(a))
# <class 'str'>
a = np.str_(a)
print(type(a))
# <class 'numpy.str_'>
print(-456%256)