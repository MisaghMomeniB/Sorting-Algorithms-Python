def bubble_sort(arr, descending=False):
    """
    Bubble Sort Algorithm with an optional descending order.

    Parameters:
    arr (list): The list of elements to be sorted.
    descending (bool): If True, sorts the list in descending order. Default is False (ascending).

    Returns:
    list: The sorted list.
    """

    n = len(arr)  # Get the length of the array

    for i in range(n):
        swapped = False  # Flag to check if any swap is made in the current pass

        # Inner loop for comparing and swapping adjacent elements
        # The last i elements are already sorted, so we reduce the range
        for j in range(0, n - i - 1):
            # Compare elements based on sorting order (ascending or descending)
            if (arr[j] > arr[j + 1] and not descending) or (arr[j] < arr[j + 1] and descending):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap the elements
                swapped = True  # Set flag to True indicating a swap occurred

        # If no swaps occurred in the current pass, the array is already sorted
        if not swapped:
            break  # Exit the loop early to optimize performance

    return arr  # Return the sorted array