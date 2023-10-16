nums1 = [1,2,3]
nums2 = [3,4,8]

def findMedianSortedArrays(nums1, nums2):
    new_list = sorted(nums1 + nums2)
    m = (len(nums1) + len(nums2)) // 2

    if len(new_list) % 2 == 0:
        median = (new_list[m-1] + new_list[m])/2
        return median
    else:
        return new_list[m]





print(findMedianSortedArrays(nums1,nums2))