arr = [-1,0,3,5,9,12]
first , end = 0, len(arr) - 1
k = 9
i = 0
'''while first <= end:
    midpoint = first + (end - first) // 2
    if arr[midpoint] ==  k :
        print(midpoint)
        exit()
    elif arr[midpoint] > k :
        end = midpoint
    else :
        first = midpoint
        '''
print((first + end)//2)