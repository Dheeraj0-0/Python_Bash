#2. count vowels in a string 

str = "hello world "

count=0
for i in str:
    if i.lower() in {a,e,i,o,u}:
        count +=1

print(count)