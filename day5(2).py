name='이해빈'

if name=='이해빈':
    print('반가워요', name)

if name=='이해빈':
    print('당신이 이해빈이군요!')
elif name=='호박':
    print('당신이 호박이군요!')
else:
    print('누구세요?')


count=0
while count < 3:
    print('횟수:', count)
    count +=1

while count < 10:
    count+=1
    if count < 4:
        continue
    print('횟수:', count)
    if count==8:
        break
   
