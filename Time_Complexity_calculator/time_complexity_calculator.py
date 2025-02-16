import numpy as np
from math import log, factorial

class ComplexityEstimator:
    def __init__(self):
        # Same complexity patterns as before
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

    # Previous methods remain the same until find_best_fit
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
        """Modified find_best_fit method with better normalization handling"""
        min_error = float('inf')
        best_complexity = None
        
        # Check if all times are equal (constant time case)
        if np.allclose(times, times[0]):
            return 'O(1)'
            
        # Normalize times using a more robust method
        times_range = np.max(times) - np.min(times)
        if times_range > 0:
            times_norm = (times - np.min(times)) / times_range
        else:
            times_norm = np.zeros_like(times)
        
        for name, (func, _) in self.complexity_patterns.items():
            try:
                predicted = func(sizes)
                pred_range = np.max(predicted) - np.min(predicted)
                
                # Skip if prediction range is too small or contains invalid values
                if pred_range <= 1e-10 or not np.all(np.isfinite(predicted)):
                    continue
                    
                predicted_norm = (predicted - np.min(predicted)) / pred_range
                error = np.mean((times_norm - predicted_norm) ** 2)
                
                if error < min_error:
                    min_error = error
                    best_complexity = name
            except Exception as e:
                continue
                
        return best_complexity or 'O(n)'  # Default to O(n) if no good fit found

    def estimate_complexity(self, input_str):
        """Modified estimation method with improved decision boundaries"""
        sizes, times = self.read_input(input_str)
        growth_rate = self.calculate_growth_rate(sizes, times)
        ratio_rate = self.calculate_ratios(sizes, times)
        best_fit = self.find_best_fit(sizes, times)
        
        # Improved decision tree
        if np.allclose(times, times[0]):
            return 'O(1)'
        elif growth_rate < 0.2:
            return 'O(1)'
        elif growth_rate < 0.8:
            return 'O(log n)'
        elif growth_rate < 1.5:
            if ratio_rate > 1.1 and ratio_rate < 1.3:
                return 'O(n log n)'
            return 'O(n)'
        elif growth_rate < 2.5:
            return 'O(n^2)'
        elif growth_rate < 3.5:
            return 'O(n^3)'
        else:
            if np.all(times[1:] / times[:-1] > 1.8):  # Check for exponential growth
                return 'O(2^n)'
            return best_fit

def main():
    estimator = ComplexityEstimator()
    
    # Test cases remain the same...
    test_cases = {
        "Test Case 1 (O(1))": ("""10 0.001
20 0.001
30 0.001
40 0.001
50 0.001
60 0.001
70 0.001
80 0.001
90 0.001
100 0.001""", "O(1)"),
        
        "Test Case 2 (O(n))": ("""10 0.010
20 0.020
30 0.030
40 0.040
50 0.050
60 0.060
70 0.070
80 0.080
90 0.090
100 0.100""", "O(n)"),
        
        "Test Case 3 (O(log n))": ("""10 0.003
20 0.004
30 0.0045
40 0.005
50 0.0052
60 0.0054
70 0.0056
80 0.0058
90 0.0059
100 0.0060""", "O(log n)"),
        
        "Test Case 4 (O(n^2))": ("""10 0.100
20 0.400
30 0.900
40 1.600
50 2.500
60 3.600
70 4.900
80 6.400
90 8.100
100 10.000""", "O(n^2)"),
        
        "Test Case 5 (O(2^n))": ("""1 0.001
2 0.002
3 0.004
4 0.008
5 0.016
6 0.032
7 0.064
8 0.128
9 0.256
10 0.512""", "O(2^n)"),
        
        "Test Case 6 (O(n log n))": ("""10 0.033
20 0.086
30 0.147
40 0.213
50 0.282
60 0.354
70 0.428
80 0.503
90 0.580
100 0.658""", "O(n log n)"),
        
        "Test Case 7 (O(n^3))": ("""10 1.000
20 8.000
30 27.000
40 64.000
50 125.000
60 216.000
70 343.000
80 512.000
90 729.000
100 1000.000""", "O(n^3)")
    }
    
    # Modified verification without Unicode characters
    def verify_results(input_str, expected):
        result = estimator.estimate_complexity(input_str)
        return f"Expected: {expected}, Got: {result}, {'PASS' if expected == result else 'FAIL'}"

    print("\nVerification Results:")
    print("-" * 50)
    for test_name, (test_input, expected) in test_cases.items():
        print(f"{test_name}:", verify_results(test_input, expected))

if __name__ == "__main__":
    main()