nums = [3,7,8,9,11,23,2,4]


def twoSum(nums,target):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1,n):
            print(i,j)
            if nums[i] + nums[j] == target:
                return [i,j]
    return []


print(twoSum(nums,6))