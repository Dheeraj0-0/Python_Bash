arr = [7,4,1,5,6,9]

minum = float('inf')
profit = 0

for num in arr:
    if num < minum:
        minum = num
    else:
        profit = max(profit,num - minum)
print(profit)
