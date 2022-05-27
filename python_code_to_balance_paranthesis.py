open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]

def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        if i in close_list:
            pos = close_list.index(i)
            if len(stack)>0:
                open_list[pos] == stack[len(stack)-1]
                stack.pop()
            else:
                return "unbalanced"
    if len(stack) == 0:
        return "balanced"
    else:
        return "unbalanced"

# string = "{[]{()}}"
# print(string,"-", check(string))
#
# string = "[{}{})(]"
# print(string,"-", check(string))

string = "((("
print(string,"-",check(string))



