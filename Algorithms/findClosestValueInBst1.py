#Average time : O(logn) | Space O(logn)
#Worst time : O(n) | Space O(n)

#PROBLEM STATEMENT
#Given a bst and a target find the closest number to the target present in bst
#===========================

#APPROACH
#Take closest as infinity check the difference of root and target if it is less than the difference of target and closest than change the closest. Then check if the number is less than the target or more than it. If less than go to right if more than go to left
#===========================

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    return closest