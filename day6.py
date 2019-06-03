Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def add(num1, num2):
	return num1 + num2

>>> add(1,2)
3
>>> add(3,5)
8
>>> def mul(num1, num2):
	return num1+num2, num1*num2

>>> mul(1,2)
(3, 2)
>>> add, mul = mul(1,2)
>>> add
3
>>> mul
2
>>> import random
>>> stu=['이','박','김']
>>> print(random.choice(stu))
이
>>> 
>>> 
>>> print(random.choice(stu))
김
>>> 
>>> 
>>> 
>>> print(random.choice(stu))
이
>>> 
>>> print(random.choice(stu))
박
>>> 
>>> print(random.choice(stu))
김
>>> 
>>> print(random.choice(stu))
김
>>> 
>>> print(random.choice(stu))
이
>>> 
>>> print(random.sample(stu,2))
['박', '이']
>>> print(random.sample(range(1,46),6))
[10, 39, 41, 6, 8, 43]
>>> random.randint(8,10)
8
>>> random.randint(8,10)
10
>>> random.randint(8,10)
10
>>> random.randint(8,10)
9
>>> random.randint(8,10)
10
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2019, 1, 20, 0, 6, 40, 65730)
>>> print(datetime.datetime.now())
2019-01-20 00:07:01.830226
>>> 
