# Given an integer x, return true if x is a palindrome, and false otherwise.

def run_test_case():
    cases = [(121, True),
             (-121, False),
             (10, False)]

    for i, (x, output) in enumerate(cases, start=1):
        result = palindrome_checker(x)
        print(f"--> Tase Case {i} <--")
        print(f"x: {x}")
        print(f"output: {result}")
        print(f"Expected: {output}")
        print("status: Passed" if result == output else "status: Failed")

def palindrome_checker(x):
    y = x
    reverse = 0

    while y > 0:
        digit = y % 10
        y = y // 10
        reverse = reverse * 10 + digit

    if reverse == x:
        return True
    else:
        return False

run_test_case()