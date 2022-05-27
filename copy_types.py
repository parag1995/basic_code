import copy

# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.copy(old_list)
#
# old_list.append([4,4,4])
# old_list[1][1]="AA"
# new_list.append([5,5,5])
# new_list[1][2]="bb"
# print(old_list)
# print(new_list)

# deep_old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# deep_new_list = copy.deepcopy(deep_old_list)
# deep_old_list.append([4,4,4])
# deep_old_list[1][1]="AA"
# deep_new_list.append([5,5,5])
# deep_new_list[1][2] = "BB"
#
# print(deep_old_list)
# print(deep_new_list)


s = "geeksforgeeks"
print(len(s))
s_new = s[0::-1]
print(s_new)
