def add_two_small_int_numbers(a, b):
    branch = []
    if not isinstance(a, int) or not isinstance(b, int):
        branch.append("A")
        return None, branch
    elif a >= 0 and a <= 100 and b >= 0 and b <= 100:
        branch.append("B")
        return a + b, branch
    branch.append("C")
    return None, branch
