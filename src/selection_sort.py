def selection_sort(arr):
    n = len(arr)  # Get the length of the array

    # Loop through the array
    for i in range(n):
        min_idx = i  # Assume the current index has the minimum value

        # Find the index of the minimum element in the remaining unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Update the index of the minimum element

        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr  # Return the sorted array