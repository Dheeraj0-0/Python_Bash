def maxSum(arr,k):
    left = 0
    maxSum = float('-inf')
    cursum = 0
    for right in range(len(arr)):
        cursum += arr[right]
        
        windowlength = right - left + 1
        if windowlength == k:
            maxSum = max(maxSum,cursum)
            cursum -= arr[left]
            left += 1
    return maxSum

print(maxSum([2, 1, 5, 1, 3, 2],3))