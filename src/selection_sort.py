def selection_sort(arr, descending=False):
    """
    Selection Sort Algorithm with an optional descending order.

    Parameters:
    arr (list): The list of elements to be sorted.
    descending (bool): If True, sorts the list in descending order. Default is False (ascending).

    Returns:
    list: The sorted list.
    """

    n = len(arr)  # Get the length of the array

    # Loop through the array
    for i in range(n):
        # Assume the current index has the minimum or maximum value
        selected_idx = i  

        # Find the index of the minimum/maximum element in the remaining unsorted portion
        for j in range(i + 1, n):
            if (arr[j] < arr[selected_idx] and not descending) or (arr[j] > arr[selected_idx] and descending):
                selected_idx = j  # Update the index of the minimum/maximum element

        # Swap the found element with the first element of the unsorted part if needed
        if selected_idx != i:
            arr[i], arr[selected_idx] = arr[selected_idx], arr[i]

    return arr  # Return the sorted array