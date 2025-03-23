def merge_sort(arr, descending=False):
    """
    Merge Sort Algorithm with an optional descending order.

    Parameters:
    arr (list): The list of elements to be sorted.
    descending (bool): If True, sorts the list in descending order. Default is False (ascending).

    Returns:
    list: The sorted list.
    """

    # Base case: If the array has only one element or is empty, return it
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle index

        # Split the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half, descending)
        merge_sort(right_half, descending)

        # Merge the sorted halves back together
        i = j = k = 0  # Initialize pointers

        # Merge elements based on sorting order (ascending or descending)
        while i < len(left_half) and j < len(right_half):
            if (left_half[i] < right_half[j] and not descending) or (left_half[i] > right_half[j] and descending):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements from left_half (if any)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements from right_half (if any)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr  # Return the sorted array