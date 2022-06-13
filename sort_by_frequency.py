# l = [1,2,3,4,3,3,3,6,7,1,1,9,3,2]
# print (sorted(l,key=l.count,reverse=True))


# lis = [1,2,3,9,4,3,3,3,6,7,1,1,3,2]
#
# dic = {}
# for num in lis:
#     if num in dic:
#         dic[num] += 1
#     else:
#         dic[num] = 1
#
# s_list = sorted(dic.items(), key=lambda x:x[1], reverse=True)
# print(s_list)
#
# new_list = []
# for num,times in s_list:
#     while times>0:
#         new_list.append(num)
#         times-=1
# print(new_list)

# from collections import Counter
# lis = "bbAa"
# c = Counter(list(lis))
# print(c)
# clist = sorted(c,key = lambda x:c[x],reverse=True)
# print(clist)
#
# op=[]
# for i in clist:
#     op.append(i*c[i])
#
# print("".join(op))


str = "dgsgsf"
ls = list(str)
print(ls)