"""
Problem 10 — Contains Duplicate

Input:

[1,2,3,1]


Output:

True    # because 1 appears twice


You must return True if ANY element repeats, else return False.

💡 Hint: Use dictionary OR set.
"""

"""
def check_duplicate(arr):
    count = {}
    for i,num in enumerate(arr):
        if num in count:
            return True
        count[num]= i
    return False



or
"""
def check_duplicate(arr):
    return len(arr) != len(set(arr))

print(check_duplicate([1,2,3,1]))