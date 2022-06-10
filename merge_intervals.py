import Tools.scripts.serve


def mergeIntervals(a):
    a.sort(key =lambda x:x[0])
    # print(a)
    s = -10000
    m = -100000
    ls=[]
    for i in range(len(a)):
        arr = a[i]
        if arr[0] > m:
            if i !=0:
                ls.append([s,m])
            m = arr[1]
            s = arr[0]
        else:
            if arr[1] >= m:
                m = arr[1]
    if m != -100000 and [s, m] not in ls:
        ls.append([s, m])
    return ls





arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
print(mergeIntervals(arr))
