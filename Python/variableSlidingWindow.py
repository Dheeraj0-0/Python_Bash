def longest_subarray_sum_k(arr, k):
    left = 0
    cursum = 0
    maxlen = 0
    for right in range(len(arr)):
        cursum += arr[right]

        while cursum > k:
            cursum -= arr[left]
            left += 1
        maxlen = max(maxlen,right-left + 1)

    return maxlen