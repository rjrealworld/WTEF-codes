def findPeak(array: [int]):
    if array[0] > array[1]:
        return array[0]
    elif array[-1] > array[-2]:
        return array[-1]
    else:
        for num in range (1, len(array) - 1):
            if array[num] > array[num - 1] and array[num] > array[num + 1]:
                return array[num]
    return 'No peak'
arr = [1, 2, 3, 4, 5, 0, -1]
print(findPeak(arr))

#Explanation
#Iterate through the array and assign the 

# Time complexity
# we iterate n times the array
# T(n) = O(n)