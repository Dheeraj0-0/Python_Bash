#Move Zeroes

#Move all zeroes to the end of the array while keeping the order of non-zero elements.

#Input:[0, 1, 0, 3, 12]

#Output:[1, 3, 12, 0, 0]

arr = [0, 1, 0, 3, 12]

j = 0  # pointer for next non-zero position

# Step 1: move all non-zero numbers to the front
for i in range(len(arr)):
    if arr[i] != 0:
        arr[j] = arr[i]
        j += 1

# Step 2: fill remaining positions with zero
while j < len(arr):
    arr[j] = 0
    j += 1

print(arr)


