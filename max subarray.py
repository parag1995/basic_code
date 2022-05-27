nums_list = [-6,-1,-5]
curr_max = 1
curr_lst = []
prev_max = 0
prev_lst = []

for i in nums_list:
    if i > 0:
        curr_max = curr_max * i

        curr_lst.append(i)
    else:
        if curr_max > prev_max:
            prev_max = curr_max
            prev_lst = curr_lst[:]

        curr_max = 1
        curr_lst = []

    print(f"ITERATION : {i} CURR MAX: {curr_max}, CURR LIST: {curr_lst}, PREV MAX: {prev_max} PREV LIST : {prev_lst}")


if prev_max > curr_max:
    print(prev_lst)

else:
    print(curr_lst)
