# nums = [2,3,-2,4,-5,-6,2]
# max_list = [0] * len(nums)
# min_list = [0] * len(nums)
# print(min_list)

def a():
    for i in range(10):
        yield(i)

b = a()
print(f"First Loop : {list(b)+list(b)}")
for i in list(b):
    print(i)
for i in b:
    print(i)
for i in b:
    print(i)