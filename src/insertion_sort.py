def insertion_sort(arr, descending=False):
    """
    Insertion Sort Algorithm with an optional descending order.

    Parameters:
    arr (list): The list of elements to be sorted.
    descending (bool): If True, sorts the list in descending order. Default is False (ascending).

    Returns:
    list: The sorted list.
    """

    # Iterate through the array starting from the second element (index 1)
    for i in range(1, len(arr)):
        key = arr[i]  # Store the current element as "key"
        j = i - 1  # Start comparing with the previous elements

        # Compare elements based on sorting order (ascending or descending)
        while j >= 0 and ((key < arr[j] and not descending) or (key > arr[j] and descending)):
            arr[j + 1] = arr[j]  # Shift the element one position ahead
            j -= 1  # Move to the previous element

        # Insert the key at the correct position
        arr[j + 1] = key  

    return arr  # Return the sorted array