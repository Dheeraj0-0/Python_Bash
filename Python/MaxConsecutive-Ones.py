# sum 1's

input = [1,1,0,1,1,1,0]

total1 = 0
count = 0

for i in input:
    if i ==1:
        count+=1
        if count > total1:
            total1 = count
    else:
        #total1 = max(total1,count)
        count=0
#total1 = max(total1,count)
print(total1)
