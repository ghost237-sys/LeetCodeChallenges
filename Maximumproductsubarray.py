nums = [2,3,-2,4]

def maxSubArray(nums):
    maxProduct = 0
    currentProduct = 1
    for num in nums:
        currentProduct *=  num

        if currentProduct > maxProduct :
            maxProduct = currentProduct

        if currentProduct < 0:
            currentProduct = 0

    return maxProduct

print(maxSubArray(nums))