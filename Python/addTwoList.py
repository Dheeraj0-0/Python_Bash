#add two list in accending order-->> time & space must be O(nm) & o(1)

list1 = [1,2,3,0,0,0]
m = 3
list2 = [1,5,9]
n=3

i = m-1
j = n - 1
k = m+n -1

while j >=0:
    if i>= 0 and list1[i] > list2[j]:
        list1[k] = list1[i]
        i-=1
    else:
        list1[k] = list2[j]
        j -= 1
    k -=1
print(list1)