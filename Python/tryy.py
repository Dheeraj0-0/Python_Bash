arr = [2, 1, 2, 4, 3]   # [4, 2, 4, -1, -1]

rev= arr[::-1]
rev.pop()
arr = rev[::-1]
print(rev)
print(arr)