def validBrackets(strr):
    matching = {")":"(","]":"[","}":"{",">":"<"}
    stack = []
    for ch in strr:
        if ch in matching:
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return len(stack) == 0

print(validBrackets("[{()}]"))
            
