arr = [2,1,2,4,3]
stack = []
result = [-1]*len(arr)

for i in range(len(arr)):
    while stack and stack[-1] < arr[-1] :
        stack.pop()
        result[i] = arr[i]
    stack.append(arr[i])
    
print(stack)
print(result)