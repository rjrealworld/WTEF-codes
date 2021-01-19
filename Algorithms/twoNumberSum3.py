#Best function
#Time complexity O(n)
#Space complexity O(n)

#PROBLEM STATEMENT
# Given a number i.e. targetSum and an array of numbers, find the pair which sums up to give targetSum else return []
# ============================================

#APPROACH
# iterate x through the array, if targetSum - x is present in the hash table return it else add x to the hash table.
# ===========================================

def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []