from unit_test import UnitTest
from program import add_two_small_int_numbers

if __name__ == "__main__":

    # Create test case
    test_case = {
        "input_list": [
            [3.2, 4],
            [3, 50.2],
            [103, 50],
            [-1, 50],
            [50, 130],
            [50, -1],
            [32, 70],
            [1, 50],
            [23, 1]
        ],
        "expected_output": [
            None,
            None,
            None,
            None,
            None,
            None,
            102,
            51,
            24
        ]
    }

    # Define unit test system
    unit_test = UnitTest(
        input_list = test_case["input_list"],
        expected_list=test_case["expected_output"],
        total_brach_nums=4
    )

    # Test program
    unit_test.test(add_two_small_int_numbers)
