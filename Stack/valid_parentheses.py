# problem description
# Given a string s which contains characters {}[]() check that it is valid
# A string is valid if every open bracket is closed by the same type of closed bracket, open brackets are closed in the correct order, and every close bracket has a corresponding open bracket of the same type
# return true if s is a valid string and false otherwise

s = input()

def isValid(s):
    if len(s) % 2 != 0:
        return False

    stack = []
    checkOpenToClose = {'}':'{', ']':'[', ')':'('}

    for c in s:
        if c in checkOpenToClose:
            if not stack:
                return False
            candidate = stack.pop()
            if candidate != checkOpenToClose[c]:
                return False
        else:
            stack.append(c)

    return True if not stack else False
