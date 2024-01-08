nums = [1,2,3,9,7,3]
target  = 6


def twoSum(nums, target):
        n = len(nums)
        for i in range(n - 1):
            print(i)
            for j in range(i + 1, n):
                #print(j)
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

print(twoSum(nums,target))