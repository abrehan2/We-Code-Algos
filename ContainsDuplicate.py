class Solution(object):
    def containsDuplicate(self, nums):
         hash = set(nums)
         if len(hash) < len(nums):
            return True
         else:
             return False;

# O(n) - Time and space complexity
