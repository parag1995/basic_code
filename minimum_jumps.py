# inp = [2,3,1,1,2,4,2,0,1,1]
inp = [2,3,1,1,4]
# inp = [3,2,1,0,4]

jumps= [0]*(len(inp)+1)

jumps[0]=0

for i in range(1,len(inp)):
    jumps[i]=float('inf')
    for j in range(i):
        if i <=j+inp[j]:

            jumps[i]=min(jumps[i],jumps[j]+1)
print(jumps)