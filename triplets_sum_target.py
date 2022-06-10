
def find_triplets(ls,num):
    lsupdated = []
    for i in range(len(ls)-1):
        new_target = num - ls[i]
        prevMap = {}
        for j in range(i+1,len(ls)):
            diff =new_target-ls[j]
            if diff in prevMap:
                lsupdated.append([i,j,prevMap[diff]])
            prevMap[ls[j]]=j
    return lsupdated



ls = [12,3,4,1,6,9]
print(find_triplets(ls,24))
