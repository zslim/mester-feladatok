import subprocess


TEST_INPUT_FILE = "test_input.csv"
DELIMITER = ","


def read_test_input():
    with open(TEST_INPUT_FILE) as file:
        lines = file.readlines()
    test_cases = []
    for i in range(1, len(lines)):
        test_file, expected_output = lines[i].split(DELIMITER)
        expected_output = expected_output.strip()
        test_cases.append({"test_input_file": test_file, "expected_output": expected_output})
    return test_cases


def run_test(test_file_name):
    with open(test_file_name) as file:
        test_input = file.read()
    test_process = subprocess.run(["python", "main.py"], input=test_input, capture_output=True, text=True)
    return test_process.stdout


def execute(test_cases):
    for case in test_cases:
        output = run_test(case["test_input_file"])
        result = "pass" if output == case["expected_output"] else "fail"
        print(f"Test case: {case['test_input_file']} \tActual: {output} \tExpected: {case['expected_output']} \tResult: {result}")


def main():
    test_cases = read_test_input()
    execute(test_cases)


if __name__ == '__main__':
    main()
