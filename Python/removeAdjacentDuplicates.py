def removeduplicates(strr):
    stack = []
    for ch in strr:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)
print(removeduplicates("azxxzy"))