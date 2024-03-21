def add_two_small_int_numbers(a, b):
    """
    Calculate sum of 2 small interger numbers which are in range 0 to 100
    Input
        a: interger number, 0 <= a <= 100
        b: interger number, 0 <= b <= 100
    Output
        Sum of a + b if they satisfy all condition else return None
    """
    
    # List to check branch test case goes through
    branch = []

    # Check a, b are integer numbers
    if not isinstance(a, int) or not isinstance(b, int):
        branch.append("A")
        return None, branch
    branch.append("B")

    # Check if a, b in range 0 to 100
    if a >= 0 and a <= 100 and b >= 0 and b <= 100:
        branch.append("C")
        return a + b, branch
    branch.append("D")

    # Otherwise, return None
    return None, branch
