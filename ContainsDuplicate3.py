nums = [1,0,1,1]

def containsNearbyAlmostDuplicate(nums,indexDiff,valueDiff):
    numshash = {}
    for i in range(len(nums)):
        numshash[i] = nums[i]

    print(numshash)
    for i in nums:
        if valueDiff - i in numshash:
            return True

        
        
    





print(containsNearbyAlmostDuplicate(nums,1,2))