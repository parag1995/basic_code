def kaydens(a):
    max_so_far = a[0]
    current_sum = 0
    st=pt=ed = 0
    for i in range(len(a)):
        current_sum = current_sum+a[i]
        if current_sum > max_so_far:
            max_so_far = current_sum
            st = pt
            ed = i
        if (current_sum<0):
            current_sum = 0
            pt=i+1
    return max_so_far,st,ed

a = [11, 10, -20, 5, -3, -5, 8, -13, 10]
max_kadane,spt,ept = kaydens(a)
print(spt,ept)
print(max_kadane)
neg_a = [-1*i for i in a]
print(neg_a)
max_negative_kayden ,start_pt, end_pt= kaydens(neg_a)
print(start_pt,end_pt)
print(max_negative_kayden)
# print(kaydens([11, 10, -20, 5, -3, -5, 8, -13, 10]))
max_wrap_val = -(sum(neg_a)-max_negative_kayden)
res = max(max_wrap_val,max_kadane)
print(res)
# for i in range(len(a))