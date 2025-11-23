def sumtarget(arr, target):

    left = 0
    right = len(arr) - 1

    while left < right:
        s = arr[left] + arr[right]

        if s == target:
            return left + 1, right + 1   # 1-based index

        elif s < target:
            left += 1     # increase sum

        else:
            right -= 1    # decrease sum

arr = [1, 2, 3, 4, 6]
target = 6
print(sumtarget(arr, target))
