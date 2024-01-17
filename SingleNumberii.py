nums = [2,2,3,2]

def singleNumber(nums):
    dct = {}
    for i in nums:
        dct[i] = dct.get(i,0) + 1

    for k,v in dct.items():
        if dct[k] == 1:
            return v


print(singleNumber(nums))