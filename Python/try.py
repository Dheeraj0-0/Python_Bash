def maxOne(arr):
    maxOne = 0
    count = 0

    for i in arr:
        if i == 1:
            count += 1
        else:
            maxOne = max(maxOne,count)
            count = 0
    return max(maxOne,count)

print(maxOne([0,1,1,0,1,1,1]))