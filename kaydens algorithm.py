def kayden(a):
    current_sum = 0
    maxsofar = a[0]
    st,ed,p = 0,0,0
    for i in range(len(a)):
        current_sum = current_sum+a[i]
        if current_sum>maxsofar:
            st = p
            ed = i
            maxsofar = current_sum
        if current_sum<0:
            p = i+1
            current_sum = 0
    return maxsofar,st,ed

print(kayden([11, 10, -20, 5, -3, -5, 8, -13, 10]))
