s = "]"

def isValid(s):
    stack_a = []
    balanced = True
    index = 0
    while index < len(s)  and balanced:
        symbol = s[index]
        if symbol in "({[":
            stack_a.append(symbol)
        else:
            if len(stack_a) == 0:
                balanced = False
            else:
                top = stack_a.pop()     
                if not matches(top,symbol):
                    balanced = False

        
        index = index + 1

    
    if len(stack_a) == 0 and balanced == True:
        return True
    else:
        return False

def matches(top,s):
    opens = "({["
    closes = ")}]"
    return opens.index(top) == closes.index(s)
 

print(isValid(s))