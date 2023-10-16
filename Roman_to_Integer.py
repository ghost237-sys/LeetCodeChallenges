s = 'CMLX'


def romanToInt(self,s):
    Roman_letters =  {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    value = 0
    for i in range(len(s)):
        if i < len(s) - 1 and Roman_letters[s[i]] < Roman_letters[s[i+1]]:
            value -= Roman_letters[s[i]]
        else:
            value += Roman_letters[s[i]]

    return value