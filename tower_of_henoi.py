def TOH(numbers,start,aux,end):
    if numbers == 1:
        print("move disk {} from {} to  {}".format(numbers,start,end))
        return
    TOH(numbers-1,start,end,aux)
    print("move disk {} from {} to  {}".format(numbers,start,end))
    TOH(numbers-1,aux,start,end)

disc= 5
TOH(disc,"A","b","c")