
import math

def nearest_neighbor(points, target):
    min_dist = float('inf')
    nearest = None
    
    for point in points:
        dist = math.sqrt((point[0] - target[0])**2 + (point[1] - target[1])**2)
        if dist < min_dist:
            min_dist = dist
            nearest = point
    
    return nearest, min_dist


def main():
    points = [(1, 2), (3, 4), (5, 6), (7, 8)]
    target = (4, 4)
    nearest, dist = nearest_neighbor(points, target)
    print(f"Points: {points}")
    print(f"Target: {target}")
    print(f"Nearest: {nearest}, Distance: {dist:.2f}")


if __name__ == "__main__":
    main()
