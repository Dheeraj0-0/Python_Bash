problem = "abcabcbb"

left = 0 
seen = set()
maxlen = 0
for right in range(len(problem)):
    while problem[right] in seen:
        seen.remove(problem[left])
        left += 1
    seen.add(problem[right])
    maxlen = max(maxlen,right - left + 1)
    
print(maxlen)