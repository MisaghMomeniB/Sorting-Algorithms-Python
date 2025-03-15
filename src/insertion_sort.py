def insertion_sort(arr):
    # Iterate through the array starting from the second element (index 1)
    for i in range(1, len(arr)):
        key = arr[i]  # Store the current element as "key"
        j = i - 1  # Start comparing with the previous elements

        # Shift elements of the sorted part of the array to the right
        # if they are greater than the key
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Move element one position ahead
            j -= 1  # Move to the previous element

        # Insert the key at the correct position
        arr[j + 1] = key

    return arr  # Return the sorted array