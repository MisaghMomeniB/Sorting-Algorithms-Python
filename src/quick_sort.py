def quick_sort(arr):
    # Base case: If the array has one or zero elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot element (middle element for better performance in some cases)
    pivot = arr[len(arr) // 2]

    # Partition the array into three lists:
    left = [x for x in arr if x < pivot]   # Elements smaller than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot

    # Recursively sort left and right, then combine with middle
    return quick_sort(left) + middle + quick_sort(right)