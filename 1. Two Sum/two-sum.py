# Given an array of integers 'nums' and an integer 'target', return indices of the two numbers such that they add up to target.

def two_sum(nums, target):
    values = {}
    for i, num in enumerate(nums):
        x = target - num
        if x in values:
            return [values[x], i]
        values[num] = i
    return None

def run_test_cases():
    cases = [([2,7,11,15], 9, [0,1]),
             ([3, 2, 4], 6, [1, 2]),
             ([3, 3], 6, [0, 1])]

    for i, (nums, target, expected) in enumerate(cases, start=1):
        result = two_sum(nums, target)

        print(f"--> Test Case {i} <--")
        print(f"Nums: {nums}")
        print(f"Target: {target}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Status: Passed" if result == expected else "Status: Failed")

run_test_cases()

