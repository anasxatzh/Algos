
# Linear_Search

# Search item of array/list by index


def linearsearch(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            print('The answer is:', i)
##            return i
##        return -1

arr = [2,5,8,7,13,17]
num = 13
print(linearsearch(arr,num))


