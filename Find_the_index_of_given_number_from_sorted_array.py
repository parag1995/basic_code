def binary_search(arr, l, r, x):

    if r >= 1:
        mid = l+(r-1)//2
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            return binary_search(arr, l, mid-1, x)

        return binary_search(arr, mid+1, r, x)
    return -1



def FndPos(arr, key):
    l, h, val = 0, 1, arr[0]
    while val<key:
        l = h
        h = 2*h
        val = arr[h]

    return binary_search(arr, l, h, key)


arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
ans = FndPos(arr,10)
if ans == -1:
    print("Element not found")
else:
    print("Element found at index", ans)