
def pair_is_equal_target(ls,target):
    prevMap = {}
    for i, n in enumerate(ls):
        diff =target-n
        if diff in prevMap:
            return [prevMap[diff],i]
        prevMap[n] = i

print(pair_is_equal_target([2,1,5,3],4))