def k_closest(points, k):
    # Function to calculate squared distance from origin
    def distance(point):
        return point[0]**2 + point[1]**2
    
    # Divide and conquer approach
    def divide_and_conquer(points):
        # Base case: if only one point, return it
        if len(points) <= 1:
            return points
        
        # Divide step: split points into two halves
        mid = len(points) // 2
        left = divide_and_conquer(points[:mid])
        right = divide_and_conquer(points[mid:])
        
        # Conquer and combine step: merge the two sorted halves
        return merge(left, right)
    
    # Merge two sorted lists based on distance
    def merge(left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if distance(left[i]) <= distance(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # Add remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    # Sort all points by distance using divide and conquer
    sorted_points = divide_and_conquer(points)
    
    # Return the k closest points
    return sorted_points[:k]

# Read input
def main():
    k = int(input().strip())
    points = []
    
    # Read points until EOF
    try:
        while True:
            line = input().strip()
            if not line:
                break
            x, y = map(int, line.split())
            points.append([x, y])
    except EOFError:
        pass
    
    # Get k closest points
    result = k_closest(points, k)
    
    # Print the result
    for point in result:
        print(point[0], point[1])

if __name__ == "__main__":
    main()