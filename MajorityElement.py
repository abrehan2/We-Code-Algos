def majorityElement(self, nums):

    temp = 0
    i = 0
    while i < len(nums):
        if nums[i] == nums[i+1]:
            temp = nums[i]
        i = i+1

    return temp
