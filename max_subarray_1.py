ls = [-1,2,5,8,-9,10]
ls1 = []
ls2 = []
max = 1
max2 = 0
prod = 1

for i in ls:
    if i>0:
        prod = prod*i
        max = prod
        ls1.append(i)

    else:
        if max > max2:
            max2 = max
            ls2 = ls1[:]
        max = 1
        ls1=[]
if max2>max:
    print(ls1)
else:
    print(ls2)