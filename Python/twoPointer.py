def two_sum_sorted(arr, target):
    left , right = 0 , len(arr) - 1
    while right > left:
        cursum = arr[left] + arr[right]
        if cursum == target:
            return left , right
        elif cursum > target:
            right -= 1
        else:
            left += 1
    return -1,-1

def reverse_array(arr):
    left , right = 0 , len(arr) - 1
    while right > left:
        arr[left], arr[right] = arr[right], arr[left]
    return arr
def is_palindrome(arr):
    left , right = 0 , len(arr) - 1
    while right > left:
        if arr[left] != arr[right]:
            return False
        left +=1
        right -= 1
    return True
