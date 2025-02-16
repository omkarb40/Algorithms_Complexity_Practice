import time
import random

def generate_test_cases():
    def linear_search(arr, target):
        """O(n) - Linear Search"""
        time.sleep(0.001 * len(arr))
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

    def bubble_sort(arr):
        """O(n^2) - Bubble Sort"""
        n = len(arr)
        time.sleep(0.0001 * n * n)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def nested_loops(n):
        """O(n^3) - Triple nested loops"""
        time.sleep(0.00001 * n * n * n)
        count = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    count += 1
        return count

    def measure_execution_time(func, *args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        return end_time - start_time

    # Input sizes
    sizes = [1] + list(range(10, 101, 10))

    # Test Case 1: Linear Search O(n)
    print("\nTest Case 1: Linear Search (Expected O(n))")
    for size in sizes:
        arr = list(range(size))
        target = size - 1
        time_taken = measure_execution_time(linear_search, arr, target)
        print(f"{size} {time_taken:.6f}")

    # Test Case 2: Bubble Sort O(n^2)
    print("\nTest Case 2: Bubble Sort (Expected O(n^2))")
    for size in sizes:
        arr = list(range(size))
        random.shuffle(arr)
        time_taken = measure_execution_time(bubble_sort, arr.copy())
        print(f"{size} {time_taken:.6f}")

    # Test Case 3: Nested Loops O(n^3)
    print("\nTest Case 3: Triple Nested Loops (Expected O(n^3))")
    for size in sizes:
        time_taken = measure_execution_time(nested_loops, size)
        print(f"{size} {time_taken:.6f}")

if __name__ == "__main__":
    generate_test_cases()