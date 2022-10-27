# Binary search:


# Test_Case : 
arr = [1,5,2,6,3,10,40]


x = 10
#



def binarySearch(arr, low, high, x):

    if high >= low:
        mid = (low+high)//2

        if arr[mid] == x:
            return mid
        elif arr[mid]>x:
            return binarySearch(arr, low, mid-1, x)
        else:
            return binarySearch(arr, mid+1, high, x)
    else:
        return -1

res = binarySearch(arr, 0, len(arr)-1, x)

if res!= -1:
    print('Element is present at index:' + str(res))
else:
    print('Element is not present in the array')
    

