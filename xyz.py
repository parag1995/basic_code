# _var1 = [1, [2, 3], 4]
#
# str1 = ""
# print(type(_var1))
# for val in _var1:
#     if isinstance(val, )
#     temp = str(val)
#     str1 = str1+temp+" "
# print(str1)

class ListManipulation:
    def __init__(self, var1):
        self.var = var1

    def list_to_string(self):
        str1 = ""
        for val in self.var:
            tempvar = str(val)
            str1 = str1+tempvar+" "
        return str1

listvar = [1, 2, 3, 4]
ls1 =[]
obj1 = ListManipulation(listvar)
ls = list(''.join(listvar))
# for i in ls:
#     ls1.append(int(i))

print(ls)
# print(obj1.list_to_string())



# @app.route("/xyz/id",methods =["GET"])
# def testmethod():
#     return "Hello World"






