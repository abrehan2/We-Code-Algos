def removeElement(nums, val):
    k = 0

    for i in nums:
        if i != val:
            nums[k] = i
            k += 1


    return k

print(removeElement([0,1,2,2,3,0,4,2], 2))