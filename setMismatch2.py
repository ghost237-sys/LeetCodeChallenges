nums = [2,3,2]

def findErrorNums(nums):
    lst = []
    for i in range(1,len(nums)):
        if nums[0] < 2:
            if nums[i] == nums[i-1]:
                lst.append(nums[i-1])
    
    for i in range(1,len(nums)+1):
        print(i)
        if i not in nums:
            lst.append(i)

    return lst

print(findErrorNums(nums))