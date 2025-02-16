import numpy as np
from scipy.optimize import curve_fit

# Define common time complexity functions
def constant(n, a):
    return a * np.ones_like(n)

def logarithmic(n, a):
    return a * np.log2(n)

def linear(n, a):
    return a * n

def linearithmic(n, a):
    return a * n * np.log2(n)

def quadratic(n, a):
    return a * n**2

def cubic(n, a):
    return a * n**3

def exponential(n, a):
    return a * 2**n

def factorial(n, a):
    return a * np.array([np.math.factorial(int(i)) for i in n])

# Map functions to their complexity names
complexity_functions = {
    "O(1)": constant,
    "O(log n)": logarithmic,
    "O(n)": linear,
    "O(n log n)": linearithmic,
    "O(n^2)": quadratic,
    "O(n^3)": cubic,
    "O(2^n)": exponential,
    "O(n!)": factorial
}

# Function to estimate the best-fit complexity
def estimate_complexity(input_sizes, running_times):
    errors = {}
    
    for name, func in complexity_functions.items():
        try:
            params, _ = curve_fit(func, input_sizes, running_times, maxfev=10000)
            predicted = func(input_sizes, *params)
            error = np.mean((running_times - predicted)**2)
            errors[name] = error
        except Exception as e:
            # Skip complexities where fitting isn't feasible (e.g., factorial for large inputs)
            errors[name] = np.inf
    
    # Return the complexity with the smallest error
    return min(errors, key=errors.get)

# Read input from the user
def main():
    print("Enter input sizes and running times (e.g., '10 0.01'). Type 'done' when finished:")
    input_sizes = []
    running_times = []

    while True:
        line = input()
        if line.lower() == 'done':
            break
        try:
            size, time = map(float, line.split())
            input_sizes.append(size)
            running_times.append(time)
        except ValueError:
            print("Invalid input. Please enter two numbers separated by space.")

    input_sizes = np.array(input_sizes)
    running_times = np.array(running_times)

    complexity = estimate_complexity(input_sizes, running_times)
    print(f"Estimated Time Complexity: {complexity}")

if __name__ == "__main__":
    main()
