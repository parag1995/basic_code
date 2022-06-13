# inp = [2,3,1,1,2,4,2,0,1,1]
inp = [2,3,1,1,4]
l=r = 0
res = 0
farthest=0
ls= [0]*(len(inp)//2)
while r<len(inp)-1:

    for i in range(l,r+1):
        if inp[i]+i>farthest:
            ls[res] = i
        farthest = max(farthest,inp[i]+i)

    l=r+1
    r=farthest
    res+=1
print(res)
print(ls)
