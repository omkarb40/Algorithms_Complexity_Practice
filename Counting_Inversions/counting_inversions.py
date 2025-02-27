def countInversions(A, B, N):
    # Step 1: Create a mapping of movie IDs to their positions in B
    B_positions = {movie: idx for idx, movie in enumerate(B)}
    
    # Step 2: Transform A into its corresponding rankings based on B
    A_transformed = [B_positions[movie] for movie in A]
    
    # Step 3: Use Merge Sort to count inversions
    def merge_and_count(arr, temp_arr, left, mid, right):
        i = left    # Left subarray index
        j = mid + 1 # Right subarray index
        k = left    # Merged array index
        inv_count = 0

        # Merge both halves while counting inversions
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)  # Count inversions
                j += 1
            k += 1

        # Copy remaining elements
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        # Copy merged elements back to original array
        for i in range(left, right + 1):
            arr[i] = temp_arr[i]

        return inv_count

    def merge_sort_and_count(arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
            inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
            inv_count += merge_and_count(arr, temp_arr, left, mid, right)
        return inv_count

    return merge_sort_and_count(A_transformed, [0] * N, 0, N - 1)

# Example Execution
A = [3, 1, 2]
B = [2, 3, 1]
N = 3

print(countInversions(A, B, N))  # Output: 2