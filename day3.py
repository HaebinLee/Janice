Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> std=['이', '김', '박']
>>> std.append('최')
>>> std
['이', '김', '박', '최']
>>> std[0]
'이'
>>> del std[0]
>>> std
['김', '박', '최']
>>> std.append('이')
>>> std
['김', '박', '최', '이']
>>> std[0:1]
['김']
>>> std[1:3]
['박', '최']
>>> std.sort()
>>> std
['김', '박', '이', '최']
>>> std.append('박')
>>> std
['김', '박', '이', '최', '박']
>>> std.count('박')
2
>>> std.count('리')
0
>>> len(std)
5
>>> my_tuple=()
>>> my_tuple
()
>>> my_tuple=1,2,3
>>> type(my_tuple)
<class 'tuple'>
>>> num1, num2, num3 = my_tuple
>>> num1
1
>>> num2
2
>>> num3
3
>>> num2=1
>>> num2
1
>>> my_tuple
(1, 2, 3)
>>> num1, num2, num3 = my_tuple
>>> num1
1
>>> num2
2
>>> num3
3
>>> num1, num2 = num2, num1
>>> my_tuple
(1, 2, 3)
>>> num1
2
>>> num2
1
>>> for std in std:
	print(std)

	
김
박
이
최
박
>>> for num in [1,2,3]:
	print(num)

	
1
2
3
>>> for str in "할로우"
SyntaxError: invalid syntax
>>> for str in "할로우":
	print(str)

	
할
로
우
>>> range(3)
range(0, 3)
>>> type(range(3))
<class 'range'>
>>> for n in range(0,3):
	print(n)

	
0
1
2
>>> for n in range(1,101):
	print(n)

	
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
>>> for n in range(3)
SyntaxError: invalid syntax
>>> for n in range(3):
	print(n)

	
0
1
2
>>> for n in range(1:3):
	
SyntaxError: invalid syntax
>>> for n in range(1,3):
	print(n)

	
1
2
>>> 
