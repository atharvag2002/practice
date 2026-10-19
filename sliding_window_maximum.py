
from collections import deque

def sliding_window_maximum(nums, k):
    if not nums or k == 0:
        return []
    
    result = []
    dq = deque()
    
    for i in range(len(nums)):
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result


def main():
    test_cases = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3),
        ([1, 2, 3, 4, 5], 2),
        ([9, 11], 2)
    ]
    for arr, k in test_cases:
        print(f"Array: {arr}, k={k}")
        print(f"Max in windows: {sliding_window_maximum(arr, k)}")


if __name__ == "__main__":
    main()
