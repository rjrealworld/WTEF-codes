#Second best function
#Time complexity O(nlogn)
#Space complexity O(1)

#PROBLEM STATEMENT
# Given a number i.e. targetSum and an array of numbers, find the pair which sums up to give targetSum else return []
# ============================================

#APPROACH
# Sort the array. Take two pointers left (index = 0) and right (last index) if they sums up to targetSum return it, if sun is less than targetSum increase left else decrease right
# ===========================================

def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []