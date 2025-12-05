arr = [2,3,5,1,4]

k = 3
left = 0
maxsum = 0
currentsum = 0
for right in range(len(arr)):
    currentsum += arr[right]
    if right - left + 1 == k:
        maxsum = max(maxsum,currentsum)
        currentsum -= arr[left]
        left += 1
print(maxsum)