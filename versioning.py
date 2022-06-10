
class Solution:
    def compareversion(self,v1,v2):
        v1 = [int(v) for v in v1.split(".")]
        v2 = [int(v) for v in v2.split(".")]
        for i in range(max(len(v1),len(v2))):
            v1_up = v1[i] if i<len(v1) else 0
            v2_up = v2[i] if i<len(v2) else 0
        print(v1_up)
        print(v2_up)





ob1 = Solution()
print(ob1.compareversion("1.0.1","1.0"))
print(ob1.compareversion("1.0.0","1.0"))
print(ob1.compareversion("1.0.0","2.0"))