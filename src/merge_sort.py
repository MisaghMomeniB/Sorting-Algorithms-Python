def merge_sort(arr):
    # Base case: If the array has only one element or is empty, return it
    if len(arr) > 1:
        # Find the middle index of the array
        mid = len(arr) // 2

        # Split the array into two halves
        left_half = arr[:mid]  # Left part
        right_half = arr[mid:]  # Right part

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves back together
        i = j = k = 0  # Initialize pointers for left_half, right_half, and arr

        # Merge elements from left_half and right_half in sorted order
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]  # Copy from left_half
                i += 1
            else:
                arr[k] = right_half[j]  # Copy from right_half
                j += 1
            k += 1  # Move to the next position in arr

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