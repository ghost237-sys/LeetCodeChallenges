nums = [-1,0,3,5,9,12]

def search(nums,target):
    start,end = 0,len(nums)- 1

    while start <= end :
        mid_position = (start + end) // 2
        if nums[mid_position] == target:
            return mid_position
        elif nums[mid_position] < target:
            start =  mid_position + 1
        else:
            end = mid_position - 1
    return -1

print(search(nums,9))

