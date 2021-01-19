def findPeak(array: [int], length: int) -> int :
    peak = array[int(length / 2)]
    if length == 1:
        return peak
    if array[int(length / 2)] < array[int(length / 2) - 1]:
        return findPeak(array[:int(length / 2)], int(length / 2))
    elif array[int(length / 2)] < array[int(length / 2) + 1]:
        return findPeak(array[int(length / 2) + 1:], int(length / 2))
    else:
        return peak

arr = [1, 2, 3, 4, 5, 0, -1]
print(findPeak(arr, len(arr)))

# Time complexity:
# For 1 element we check 0 times
# for 2 elements we check 1 time
# for 4 elements we check 2 times
# T(n) = O(log2 (n))