nums = [2,3,-2,4]

def maxSubArray(nums):
    maxSum = 0
    currentSum = 1
    for num in nums:
        currentSum *=  num

        if currentSum > maxSum :
            maxSum = currentSum

        if currentSum < 0:
            currentSum = 0

    return maxSum

print(maxSubArray(nums))