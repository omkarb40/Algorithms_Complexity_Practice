import numpy as np
import time
import random
from math import log, factorial

class ComplexityEstimator:
    def __init__(self):
        self.complexity_patterns = {
            'O(1)': (lambda n: 1, 0),
            'O(log n)': (lambda n: np.log2(n), 0.5),
            'O(n)': (lambda n: n, 1),
            'O(n log n)': (lambda n: n * np.log2(n), 1.2),
            'O(n^2)': (lambda n: n**2, 2),
            'O(n^3)': (lambda n: n**3, 3),
            'O(2^n)': (lambda n: 2**n, float('inf')),
            'O(n!)': (lambda n: np.array([factorial(int(x)) for x in n]), float('inf'))
        }

    def read_input(self, input_str):
        lines = input_str.strip().split('\n')
        sizes = []
        times = []
        for line in lines:
            n, t = map(float, line.split())
            sizes.append(n)
            times.append(t)
        return np.array(sizes), np.array(times)

    def calculate_growth_rate(self, sizes, times):
        log_sizes = np.log2(sizes)
        log_times = np.log2(times)
        slope, _ = np.polyfit(log_sizes, log_times, 1)
        return slope

    def calculate_ratios(self, sizes, times):
        time_ratios = times[1:] / times[:-1]
        size_ratios = sizes[1:] / sizes[:-1]
        growth_ratios = np.log2(time_ratios) / np.log2(size_ratios)
        return np.mean(growth_ratios)

    def find_best_fit(self, sizes, times):
        min_error = float('inf')
        best_complexity = None
        
        times_norm = (times - np.min(times)) / (np.max(times) - np.min(times))
        
        for name, (func, _) in self.complexity_patterns.items():
            try:
                predicted = func(sizes)
                denominator = np.max(predicted) - np.min(predicted)
                if denominator == 0 or not np.isfinite(denominator):
                    continue
                predicted_norm = (predicted - np.min(predicted)) / denominator
                
                if not np.all(np.isfinite(predicted_norm)):
                    continue
                    
                error = np.mean((times_norm - predicted_norm) ** 2)
                
                if error < min_error:
                    min_error = error
                    best_complexity = name
            except Exception as e:
                continue
                
        return best_complexity

    def estimate_complexity(self, input_str):
        sizes, times = self.read_input(input_str)
        growth_rate = self.calculate_growth_rate(sizes, times)
        ratio_rate = self.calculate_ratios(sizes, times)
        best_fit = self.find_best_fit(sizes, times)
        
        if growth_rate < 0.2:
            return 'O(1)'
        elif growth_rate < 0.8:
            return 'O(log n)'
        elif growth_rate < 1.5:
            return 'O(n)' if ratio_rate < 1.5 else 'O(n log n)'
        elif growth_rate < 2.2:
            return 'O(n^2)'
        elif growth_rate < 2.8:
            return 'O(n^3)'
        else:
            return best_fit

def generate_test_cases():
    def linear_search(arr, target):
        """O(n) - Linear Search"""
        # Time proportional to size
        time.sleep(0.001 * len(arr))  # Delay proportional to n
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

    def bubble_sort(arr):
        """O(n^2) - Bubble Sort"""
        n = len(arr)
        # Time proportional to size squared
        time.sleep(0.0001 * n * n)  # Delay proportional to n^2
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def nested_loops(n):
        """O(n^3) - Triple nested loops"""
        # Time proportional to size cubed
        time.sleep(0.00001 * n * n * n)  # Delay proportional to n^3
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

    # Input sizes - using smaller sizes for cubic complexity
    sizes = [1] + list(range(10, 101, 10))
    test_cases = {}

    # Test Case 1: Linear Search O(n)
    linear_times = []
    print("\nTest Case 1: Linear Search (Expected O(n))")
    print("Size    Time")
    print("-" * 20)
    for size in sizes:
        arr = list(range(size))
        target = size - 1  # Worst case: target at the end
        time_taken = measure_execution_time(linear_search, arr, target)
        linear_times.append(time_taken)
        print(f"{size:<7} {time_taken:.6f}")
    test_cases['Linear Search'] = (sizes, linear_times)

    # Test Case 2: Bubble Sort O(n^2)
    bubble_times = []
    print("\nTest Case 2: Bubble Sort (Expected O(n^2))")
    print("Size    Time")
    print("-" * 20)
    for size in sizes:
        arr = list(range(size))
        random.shuffle(arr)  # Randomize array
        time_taken = measure_execution_time(bubble_sort, arr.copy())
        bubble_times.append(time_taken)
        print(f"{size:<7} {time_taken:.6f}")
    test_cases['Bubble Sort'] = (sizes, bubble_times)

    # Test Case 3: Nested Loops O(n^3)
    nested_times = []
    print("\nTest Case 3: Triple Nested Loops (Expected O(n^3))")
    print("Size    Time")
    print("-" * 20)
    for size in sizes:
        time_taken = measure_execution_time(nested_loops, size)
        nested_times.append(time_taken)
        print(f"{size:<7} {time_taken:.6f}")
    test_cases['Nested Loops'] = (sizes, nested_times)

    return test_cases

def main():
    # Create complexity estimator
    estimator = ComplexityEstimator()
    
    # Generate test cases
    print("Generating and analyzing test cases...")
    test_cases = generate_test_cases()
    
    # Analyze each test case
    print("\nComplexity Analysis Results:")
    print("=" * 50)
    
    for algorithm, (sizes, times) in test_cases.items():
        # Format input for the estimator
        input_str = "\n".join(f"{size} {time}" for size, time in zip(sizes, times))
        
        # Get estimated complexity
        estimated = estimator.estimate_complexity(input_str)
        
        # Determine expected complexity
        expected = {
            'Linear Search': 'O(n)',
            'Bubble Sort': 'O(n^2)',
            'Nested Loops': 'O(n^3)'
        }[algorithm]
        
        # Print results
        print(f"\nAlgorithm: {algorithm}")
        print(f"Expected Complexity: {expected}")
        print(f"Estimated Complexity: {estimated}")
        print(f"Correct: {'Yes' if expected == estimated else 'No'}")

if __name__ == "__main__":
    main()