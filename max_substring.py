
def longestsubstring(st):
    l= 0
    res = 0
    charset = set()
    ls = []

    for i in range(len(st)):
        while st[i] in charset:
                charset.remove(st[l])
                l+=1
        charset.add(st[i])
        res = max(res,i-l+1)
    return res,ls



st = "abcdbcbb"
print(longestsubstring(st))