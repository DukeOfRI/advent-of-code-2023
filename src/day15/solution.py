from helpers import read_file


def convert_string_to_list_of_ascii(input_string: str) -> list[int]:
    return [ord(i) for i in input_string]


def run_hash_algorithm(ascii_values: list[int]) -> int:
    current_value = 0
    for ascii_value in ascii_values:
        current_value += ascii_value
        current_value *= 17
        current_value %= 256
    return current_value


def calculate_hash(puzzle_input_file_name: str) -> int:
    puzzle_input = read_file(puzzle_input_file_name)
    input_list = puzzle_input.split(",")
    output_list = []
    for i in input_list:
        ascii_values = convert_string_to_list_of_ascii(i)
        output_list.append(run_hash_algorithm(ascii_values))
    return sum(output_list)


def test_calculate_hash__example_1():
    # GIVEN the puzzle input from example 1
    # WHEN the function is called
    # THEN output from the example is returned
    assert calculate_hash("example_1.txt") == 52


def test_calculate_hash__example_2():
    # GIVEN the puzzle input from example 2
    # WHEN the function is called
    # THEN output from the example is returned
    assert calculate_hash("example_2.txt") == 1320


output = calculate_hash("exercise.txt")
