number = 11208

def check_zeros(number):
    lst = [int(i) for i in str(number)]
    x = set()
    for i in lst[1:]:
        x.add(i)
    if len(x) == 1:
        return True


def check_increment(number):
    lst = [int(i) for i in str(number)]
    if lst == sorted(lst):
        return True

def check_decrement(number):
    lst = [int(i) for i in str(number)]
    if lst == sorted(lst,reverse=True):
        return True

def check_palindrome(number):
    lst = [int(i) for i in str(number)]
    if lst == lst[::-1]:
        return True


def is_interesting(number,awesome_phrases):
    if len(str(number)) < 3:
        return 0
    if check_zeros(number):
        return 2
    elif check_increment(number):
        return 2
    elif check_decrement(number):
        return 2
    elif check_palindrome(number):
        return 2 
    else:
        st = ()
        st2 = ()
        st3 = ()
        for i in number:
            st.add(i)
        for i in str(awesome_phrases[0]):
            st2.add(i)
        for i in str(awesome_phrases[1]):
            st3.add(i)
        st4 = st.union(st2)
        st5 = st.union(st3)
        if len(st4) > 1 or len(st5) > 1:
            return 1
        else:
            return 0
    

print(is_interesting(number,[1337,256]))