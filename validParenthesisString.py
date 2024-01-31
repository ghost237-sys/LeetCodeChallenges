s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"


def checkValidString(s):
    cmax = 0
    cmin = 0
    for i in s:
        if i == "(":
            cmax += 1
            cmin += 1
        if i == ")":
            cmax -= 1
            cmin = max(cmin-1,0)
        if i == "*":
            cmax += 1
            cmin = max(cmin-1,0)

    return cmin == 0

print(checkValidString(s))