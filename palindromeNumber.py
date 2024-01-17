x = 121


def isPalindrome(x):
    
    lst = []
    for i in str(x):
        lst.append(i)

    if lst == lst[::-1]:
        return True
    else:
        return False
    

print(isPalindrome(x))