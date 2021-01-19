#Worst function
#Time complexity O(n^2)
#Space complexity O(1)

#PROBLEM STATEMENT
# Given a number i.e. targetSum and an array of numbers, find the pair which sums up to give targetSum else return []
# ============================================

#APPROACH
# loop through the array taking 2 numbers at a time and check if it is equal to the targetSum or not
# ===========================================

def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range (i + 1, len(array)):
            secondNum = array[j]
            if array[i] + array[j] == targetSum:
                return [firstNum, secondNum]
    return []