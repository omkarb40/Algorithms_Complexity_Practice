def k_closest(points, k):
    def distance(point):
        return point[0]**2 + point[1]**2
    
    def divide_and_conquer(points):
        if len(points) <= 1:
            return points
        
        mid = len(points) // 2
        left = divide_and_conquer(points[:mid])
        right = divide_and_conquer(points[mid:])
        
        return merge(left, right)
    
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
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    sorted_points = divide_and_conquer(points)
    
    return sorted_points[:k]

def main():
    k = int(input().strip())
    points = []
    
    try:
        while True:
            line = input().strip()
            if not line:
                break
            x, y = map(int, line.split())
            points.append([x, y])
    except EOFError:
        pass
    
    result = k_closest(points, k)
    
    for point in result:
        print(point[0], point[1])

if __name__ == "__main__":
    main()