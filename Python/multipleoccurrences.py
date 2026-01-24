arr = [1,2,4,1,5,6,7,1,9]
#output --> [0,3,7]  -->3
target = 1
indexx=[]
for i,num in enumerate(arr):
    if num == target:
        indexx.append(i)

print(f"indexx...{indexx},occurence ---> {len(indexx)}")