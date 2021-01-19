#Average time : O(logn) | Space O(1)
#Worst time : O(n) | Space O(1)

#PROBLEM STATEMENT
#Given a bst and a target find the closest number to the target present in bst
#===========================

#APPROACH
#Take closest as infinity check the difference of root and target if it is less than the difference of target and closest than change the closest. Then check if the number is less than the target or more than it. If less than go to right if more than go to left
#===========================

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest