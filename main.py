from unit_test import UnitTest
from program import add_two_small_int_numbers

if __name__ == "__main__":
    test_case = {
        "input_list": [
            # [3.2, 4],
            [-5, 10],
            [-10, -2],
            [102, 50],
            [105, 107],
            [43, 27],
            [50, 76]
        ],
        "expected_output": [
            # None,
            None,
            None,
            None,
            None,
            70,
            126
        ]
    }

    unit_test = UnitTest(
        input_list = test_case["input_list"],
        expected_list=test_case["expected_output"],
        total_brach_nums=3
    )

    unit_test.test(add_two_small_int_numbers)
