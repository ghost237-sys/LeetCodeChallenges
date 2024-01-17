nums  = [5,1,3]
target = 3

def search(nums,target): 
    start = 0
    end = len(nums) - 1
    
    while start <= end:
        mid = (start + end) // 2
       
        if nums[mid] == target:
            return mid
        
        if nums[start] <= target:
            if nums[start] <= target and target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid ] > target and target <= nums[end]:
                start = mid + 1
            if nums[mid] < target and target <= nums[end]:
                end = mid - 1
            else:
                end = mid - 1

        
    return -1



     

print(search(nums,target))

