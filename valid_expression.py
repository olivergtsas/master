
syms = {'(':')', '[':']' , '{':'}' }

s = "(())[]{(())([]{})}"

stack=[]


def validity(s):
    stack = []

    stack.append(s[0])
    
    for sym in s[1:]:
        if stack and sym == syms.get(stack[-1]):
            stack.pop()
        else:
            stack.append(sym)
    if not stack:
        return  'valid'
    else:
        return 'not valid'
    
    
print(validity(s))