nums = [2,3,2]

def findErrorNums(nums):
    lst = []
    dct = {}
    for i in nums:
        dct[i] = dct.get(i,0) + 1
    for k,v in dct.items():
        if v == 2:
            lst.append(k)

    for i in range(1,len(nums)+1):
        if i not in nums:
            lst.append(i)
        
    return lst

print(findErrorNums(nums))