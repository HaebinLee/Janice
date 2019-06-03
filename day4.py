# 28 구구단 출력
#for j in range(2,10):
#    for i in range(1,10):
#        print('{}x{}={}'.format(j,i,j*i))


# 29
numbers=[1,2,3,4,5,6,7,8,9,10]

odd_numbers=[]
for number in numbers:
    if number % 2 ==1:
        odd_numbers.append(number)
print(odd_numbers)

#comprehension
odd_numbers=[number for number in numbers if number % 2 ==1]
print(odd_numbers)

# 30
count=0

count=count+1
count +=1

count = count -1
count -= 1

#31
3 + 3
20 - 5
3**2
7//3
7%3

#32
if 1%2 ==1:
    print("홀수")
if 2%2 ==0:
    print("짝수")
    
for number in numbers:
    if number % 2 ==1:
        print(number, "홀수")
    else:
        print(number, "짝수")
        
        


