Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> print('Hello') #안녕?
Hello
>>> #3+4
>>> 3+4
7
>>> my_str="하이"
>>> print(my_str)
하이
>>> type(my_str)
<class 'str'>
>>> my_str='바이'
>>> type(my_str)
<class 'str'>
>>> my_str='''누구야
안녕
올'''
>>> my_str
'누구야\n안녕\n올'
>>> my_str='My name is %s' % 'Haebin'
>>> my_str
'My name is Haebin'
>>> '%d %f' % (1, 3)
'1 3.000000'
>>> '%f' %3.14
'3.140000'
>>> 'My name is {}'.format('이해빈')
'My name is 이해빈'
>>> '{} x {} = {}'.format(2,3,2*3)
'2 x 3 = 6'
>>> '{1} x {0} = {2}.'.format(2,3,2*3)
'3 x 2 = 6.'
>>> my_name='Haebin'
>>> my_name[0]
'H'
>>> my_name[-1]
'n'
>>> slice(my_name)
slice(None, 'Haebin', None)
>>> slice(my_name)[0:1]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    slice(my_name)[0:1]
TypeError: 'slice' object is not subscriptable
>>> my_name[0:1]
'H'
>>> my_name[:3]
'Hae'
>>> what='세미나 시계열 역학'
>>> what.split()
['세미나', '시계열', '역학']
>>> what='세미나,시계열,역학'
>>> what.split(,)
SyntaxError: invalid syntax
>>> what.split(',')
['세미나', '시계열', '역학']
>>> """이것도 주석입니다"""
'이것도 주석입니다'
>>> print('집단지성')
집단지성
>>> print('집단지성', end='/')
집단지성/
>>> print(1+3, end='입니다')
4입니다
>>> print('안녕\n하세요')
안녕
하세요
>>> print('안녕', end='\t'); print('하세요')
안녕	하세요
>>> my_list=[]
>>> my_list
[]
>>> type(my_list)
<class 'list'>
>>> my_list=[1,2,3]
>>> 
