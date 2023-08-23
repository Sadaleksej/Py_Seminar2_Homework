import math
s = int(input("Введите сумму S: "))
p = int(input("Введите произведение P: "))

d = s*s - 4*p
if d<0:
    print(f"Отсуствуют такие целые числа!")
    exit()

a1 = (s+math.sqrt(d))/2
a2 = (s-math.sqrt(d))/2
b1 = s-a1
b2 = s-a2

if(a1*10%10==0) and (b1*10%10==0):
    print(f"Искомые числа: {int(a1)} и {int(b1)}")    
elif(a2*10%10==0) and (b2*10%10==0):
    print(f"Искомые числа: {int(a2)} и {int(b2)}")
else:
    print(f"Отсуствуют такие целые числа!")        