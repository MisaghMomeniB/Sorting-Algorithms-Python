import random

def quick_sort(arr, descending=False):
    """
    Quick Sort Algorithm with an optional descending order.

    Parameters:
    arr (list): The list of elements to be sorted.
    descending (bool): If True, sorts the list in descending order. Default is False (ascending).

    Returns:
    list: The sorted list.
    """

    # Base case: If the array has one or zero elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot element (random choice helps prevent worst-case scenarios)
    pivot = random.choice(arr)

    # Partition the array into three lists based on pivot
    left = [x for x in arr if x < pivot]   # Elements smaller than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot

    # Recursively sort left and right, then combine with middle
    if descending:
        return quick_sort(right, descending) + middle + quick_sort(left, descending)
    else:
        return quick_sort(left, descending) + middle + quick_sort(right, descending)