

str =  "A man, a plan, a canal: Panama"

cleanstr=""
for i in str:
    if i.isalpha():
        cleanstr += i.lower()
revstr = cleanstr[::-1]
if cleanstr == revstr:
    print(True)
else:
    print(False)