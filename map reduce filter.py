import functools

is_even = lambda x: x % 2 == 0

nums = [3,2,6,8,4,6,2,9]
evens =list(filter(is_even,nums))
doubles = list(map(lambda x:x*2, evens))
print(functools.reduce(lambda a, b: a+b, nums))
print(evens)
print(doubles)
