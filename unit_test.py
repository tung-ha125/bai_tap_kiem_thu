class UnitTest():
    def __init__(self, input_list, expected_list, total_brach_nums):
        self.input_list = input_list
        self.expected_list = expected_list
        self.total_branch_nums = total_brach_nums
    
    def test(self, function):
        branch_list = []
        for index, (input, expect) in enumerate(zip(self.input_list, self.expected_list)):
            actual_output, branch = function(input[0], input[1])
            branch_list.extend(branch)
            if actual_output == expect:
                print(f"Test {index}: Passed.")
            else:
                print(f"Test {index}: Failed.")
        
        C2_coverage_score = self.compute_C2_coverage(branch_list)
        print(f"C2 coverage score: {C2_coverage_score}")
    
    def compute_C2_coverage(self, branch_list):
        return len(list(set(branch_list))) / self.total_branch_nums

