def calculateTripCost(x, y):
    # Kiểm tra điều kiện đầu vào
    if x < 0:
        return -1
    elif y < 0:
        return -1
    
    # Tính số tiền dựa trên km đi
    cost = 0
    if x <= 30:
        cost += 11000 * x
    else:
        cost += 11000 * 30 + (x - 30) * 9500

    # Tiền cước + tiền chờ đợi
    cost += (20000 * y + 9000)

    return cost

if __name__ == "__main__":
    test_cases = [
        {"ID": "TC1", "input": [-1, 2], "expected_output": -1},
        {"ID": "TC2", "input": [25, 0], "expected_output": 284000},
        {"ID": "TC3", "input": [31, 1], "expected_output": 368500},
        {"ID": "TC4", "input": [1, -1], "expected_output": -1}                
    ]

    for i in test_cases:
        actual_output = calculateTripCost(*i["input"])
        instruction = "{ID}: {status} Actual output: {output}"
        if actual_output == i["expected_output"]:
            print(instruction.format_map({"ID": i["ID"], "status": "Pass", "output": actual_output}))
        else:
            print(instruction.format_map({"ID": i["ID"], "status": "Failed", "output": actual_output}))
