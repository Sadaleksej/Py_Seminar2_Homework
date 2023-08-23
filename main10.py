n = int(input("Введите количество монеток N: "))
k = 0
m=0
i = 1
while (i <n+1):
    t = int(input(f"{i}-я монета: орел (0) или решка (1): "))
    if (t<0) or (t>1):
        print("введено некорректное значение")
        continue
    else:
        if t==0:
            k+=1
            i+=1
        else:
            m+=1
            i+=1 

if k==0 or m == 0:
    print(f"ничего переворачивать не нужно!")     
else:
    if k>m:
        print(f"нужно перевернуть {m} решек")
    else: 
        print(f"нужно перевернуть {k} орлов")
