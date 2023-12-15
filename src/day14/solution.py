import numpy as np

from helpers import read_file


def calculate_total_load_after_north_shift(puzzle_input_file_name: str) -> int:
    puzzle_input = read_file(puzzle_input_file_name)
    puzzle_input_split_per_line = puzzle_input.split("\n")
    puzzle_input_array = np.array([list(i) for i in puzzle_input_split_per_line])

    total_load = 0
    for column_index in range(puzzle_input_array.shape[1]):
        first_available_place = 0
        for index, value in enumerate(puzzle_input_array[:, column_index]):
            if value == "O":
                total_load += puzzle_input_array.shape[0] - first_available_place
                first_available_place += 1
            elif value == "#":
                first_available_place = index + 1

    return total_load


def test_total_load_after_north_shift__example():
    # GIVEN the puzzle input from the example
    # WHEN the function is called
    # THEN output from the example is returned
    assert calculate_total_load_after_north_shift("example.txt") == 136


output = calculate_total_load_after_north_shift("exercise.txt")
