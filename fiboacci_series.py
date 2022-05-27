# fibls = [0,1]
#
def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

nterms = 10
ls = []
if nterms <= 0:
    print("print +ve")
else:
    for i in range(nterms):
        ls.append(Fibonacci(i))
print(ls)

#
#

# def Fibonacci(n):
#     assert n>=0 and int(n) == n, 'Fibonacci number cannot be negative or non integer'
#     if n in [0,1]:
#         return n
#     else:
#         return (Fibonacci(n-1)+Fibonacci(n-2))
#
#
# print(Fibonacci(9))