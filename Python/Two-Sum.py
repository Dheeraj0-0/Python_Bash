arr = [2, 7, 11, 15]
target = 9

seen = {}  # value -> index

for i, num in enumerate(arr):
    complement = target - num
    
    if complement in seen:
        print(f"Indexes are: {seen[complement]}, {i}")
        break
    
    seen[num] = i
