def isValid(s):
    validLeft = {"(":")", "{":"}", "[":"]"}
    bracketStack = []
    for i in s:
        if i in validLeft:
            bracketStack.append(i)
            continue
        else:
            if bracketStack and validLeft[bracketStack[-1]] == i:
                bracketStack.pop()
                continue
            else:
                return False
    if len(s) > 1 and len(bracketStack) == 0:
        return True
    return False

print(isValid("(({[]}))"))
print(isValid("[["))
print(isValid("]]"))