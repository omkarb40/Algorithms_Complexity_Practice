import numpy as np
from math import log, factorial

class ComplexityEstimator:
    def __init__(self):
        # Dictionary mapping complexity names to their theoretical growth functions
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
        """Parse input string into arrays of sizes and times"""
        lines = input_str.strip().split('\n')
        sizes = []
        times = []
        for line in lines:
            n, t = map(float, line.split())
            sizes.append(n)
            times.append(t)
        return np.array(sizes), np.array(times)

    def calculate_growth_rate(self, sizes, times):
        """Calculate growth rate using log-log regression"""
        # Convert to log space
        log_sizes = np.log2(sizes)
        log_times = np.log2(times)
        
        # Perform linear regression
        slope, _ = np.polyfit(log_sizes, log_times, 1)
        return slope

    def calculate_ratios(self, sizes, times):
        """Calculate ratios between consecutive terms"""
        time_ratios = times[1:] / times[:-1]
        size_ratios = sizes[1:] / sizes[:-1]
        growth_ratios = np.log2(time_ratios) / np.log2(size_ratios)
        return np.mean(growth_ratios)

    def find_best_fit(self, sizes, times):
        """Find best fitting complexity using normalized curve fitting"""
        min_error = float('inf')
        best_complexity = None
        
        # Normalize times to [0,1] range
        times_norm = (times - np.min(times)) / (np.max(times) - np.min(times))
        
        for name, (func, _) in self.complexity_patterns.items():
            try:
                predicted = func(sizes)
                # Add check for division by zero
                denominator = np.max(predicted) - np.min(predicted)
                if denominator == 0 or not np.isfinite(denominator):
                    continue
                predicted_norm = (predicted - np.min(predicted)) / denominator
                
                # Check for invalid values
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
        """Main method to estimate time complexity using hybrid approach"""
        # Parse input
        sizes, times = self.read_input(input_str)
        
        # Method 1: Calculate growth rate using regression
        growth_rate = self.calculate_growth_rate(sizes, times)
        
        # Method 2: Calculate growth ratios
        ratio_rate = self.calculate_ratios(sizes, times)
        
        # Method 3: Find best fit using curve fitting
        best_fit = self.find_best_fit(sizes, times)
        
        # Combine results using a simple decision tree
        if growth_rate < 0.2:
            return 'O(1)'
        elif growth_rate < 0.8:
            return 'O(log n)'
        elif growth_rate < 1.5:
            return 'O(n)' if ratio_rate < 1.5 else 'O(n log n)'
        elif growth_rate < 2.5:
            return 'O(n^2)'
        elif growth_rate < 3.5:
            return 'O(n^3)'
        else:
            # For exponential or factorial growth, trust the curve fitting
            return best_fit

def main():
    # Example usage
    estimator = ComplexityEstimator()
    
    # Test cases
    test_input_1 = """1 0.001
10 0.010
20 0.040
30 0.090
40 0.160
50 0.250
60 0.360
70 0.490
80 0.640
90 0.810
100 1.000"""

    test_input_2 = """10 0.010
20 0.020
30 0.030
40 0.040
50 0.050
60 0.060
70 0.070
80 0.080
90 0.090
100 0.100"""

    test_input_3 = """10 0.003
20 0.004
30 0.0045
40 0.005
50 0.0052
60 0.0054
70 0.0056
80 0.0058
90 0.0059
100 0.0060"""

    test_input_4 = """10 0.100
20 0.400
30 0.900
40 1.600
50 2.500
60 3.600
70 4.900
80 6.400
90 8.100
100 10.000"""

    test_input_5 = """1 0.001
2 0.002
3 0.004
4 0.008
5 0.016
6 0.032
7 0.064
8 0.128
9 0.256
10 0.512"""

    result_1 = estimator.estimate_complexity(test_input_1)
    result_2 = estimator.estimate_complexity(test_input_2)
    result_3 = estimator.estimate_complexity(test_input_3)
    result_4 = estimator.estimate_complexity(test_input_4)
    result_5 = estimator.estimate_complexity(test_input_5)
    print(f"Estimated time complexity: {result_1}")
    print(f"Estimated time complexity: {result_2}")
    print(f"Estimated time complexity: {result_3}")
    print(f"Estimated time complexity: {result_4}")
    print(f"Estimated time complexity: {result_5}")

if __name__ == "__main__":
    main()