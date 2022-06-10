numbers = [2,8,9,11,12,26,27,29,33,36,37,42,44,46,47,52,56,57,58,60,61,64,68,70,72,73,76,77,78,80,82,83,95,96,98,99]
sum_present=0
sum_prefix = [sum_prefix[i]+numbers[i-1] for i in range(len(numbers))]
print(sum_prefix)