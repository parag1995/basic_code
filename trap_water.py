def trapwater(height):
    l,r = 0,len(height)-1
    maxleft,maxright = height[l], height[r]
    res = 0
    while l<r:
        if maxleft < maxright:
            l +=1
            maxleft = max(maxleft,height[l])
            res += maxleft -height[l]

        else:
            r-=1
            maxright = max(maxright,height[r])
            res += maxright -height[r]

    return res

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trapwater(height))