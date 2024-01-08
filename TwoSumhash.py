nums = [1,3,2,9,7,4]
target  = 6


def twoSum(nums, target):
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            print(i)
            numMap[nums[i]] = i 
           
        
        print(numMap)
        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found

print(twoSum(nums,target))

