def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

            # Increment the counter for each comparison
            merge_sort.comparison_count += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def merge_sort_with_count(arr):
    # Initialize comparison counter
    merge_sort.comparison_count = 0

    merge_sort(arr)

    return arr, merge_sort.comparison_count


# Example usage:
arr =[2,5,1,6,3,4,8,7]
sorted_arr, comparisons = merge_sort_with_count(arr)
print("Sorted array:", sorted_arr)
print("Total comparisons:", comparisons)
