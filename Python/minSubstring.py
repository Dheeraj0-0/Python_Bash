def minsubstring(arr,target):
    left = 0
    sum =0
    bestrange = (-1,-1)
    minlen = float('inf')
    for right in range(len(arr)):
        sum += arr[right]
        while sum >= target:
            if right - left + 1 < minlen :
                minlen = min(minlen,right - left + 1)
                bestrange = (left,right)
            sum -= arr[left]
            left += 1
    if minlen == float('inf'): return 0,[]
    else:
        start,end = bestrange
        return minlen ,arr[start:end + 1]
    
arr = [2,3,1,2,4,3]
target = 7
valur,substring = minsubstring(arr,target)

print(f"minimum length of sub string {valur} and substring are {substring}")