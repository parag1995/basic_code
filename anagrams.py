import collections
ls = ["eat","tea","tan","ate","nat","bat"]
dict_1 = {}
# print(dict_1)
for i in ls:
    # print("".join(sorted(i)))
    if "".join(sorted(i)) in dict_1.keys():
        dict_1["".join(sorted(i))].append(i)
    else:
        dict_1["".join(sorted(i))] = [i]
print(dict_1)