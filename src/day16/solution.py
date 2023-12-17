from copy import deepcopy

import numpy as np

from helpers import read_file


class Beam:
    def __init__(self, coordinates: tuple[int, int], direction: tuple[int, int]):
        self.coordinates = coordinates
        self.direction = direction

    def __hash__(self) -> int:
        return hash((self.coordinates, self.direction))

    def __eq__(self, other: "Beam") -> bool:
        return hash(self) == hash(other)

    def go_straight(self) -> None:
        self.coordinates = (
            self.coordinates[0] + self.direction[0],
            self.coordinates[1] + self.direction[1],
        )

    def change_direction(self, new_direction: tuple[int, int]) -> None:
        self.direction = new_direction


class BeamReflector:
    def __init__(self, beam: Beam, matrix: np.array) -> None:
        self.active_beams = [beam]
        self.matrix = matrix
        self.seen_beams = set()

    def reflect_all_beams(self):
        while self.active_beams:
            self.reflect()

    def reflect(self):
        beam = self.active_beams[0]
        if beam in self.seen_beams:
            self.active_beams.pop(0)
        else:
            self.seen_beams.add(deepcopy(beam))
            if self.will_leave_the_board(beam):
                self.active_beams.pop(0)
            else:
                beam.go_straight()
                grid_input = self.matrix[beam.coordinates[1]][beam.coordinates[0]]
                if grid_input == "/":
                    beam.change_direction((-beam.direction[1], -beam.direction[0]))
                elif grid_input == "\\":
                    beam.change_direction((beam.direction[1], beam.direction[0]))
                elif grid_input == "|" and beam.direction[0] != 0:
                    beam.change_direction((0, 1))
                    new_beam = Beam(beam.coordinates, (0, -1))
                    if new_beam not in self.seen_beams:
                        self.active_beams.append(new_beam)
                elif grid_input == "-" and beam.direction[1] != 0:
                    beam.change_direction((-1, 0))
                    new_beam = Beam(beam.coordinates, (1, 0))
                    if new_beam not in self.seen_beams:
                        self.active_beams.append(new_beam)

    def will_leave_the_board(self, beam: Beam) -> bool:
        if beam.direction[0] == -1 and beam.coordinates[0] == 0:
            return True
        if beam.direction[0] == 1 and beam.coordinates[0] == (self.matrix.shape[1] - 1):
            return True
        if beam.direction[1] == -1 and beam.coordinates[1] == 0:
            return True
        if beam.direction[1] == 1 and beam.coordinates[1] == (self.matrix.shape[0] - 1):
            return True


def main(puzzle_input_file_name: str) -> int:
    puzzle_input = read_file(puzzle_input_file_name)
    puzzle_input_split_per_line = puzzle_input.split("\n")
    puzzle_input_array = np.array([list(i) for i in puzzle_input_split_per_line])

    start_beam = Beam((-1, 0), (1, 0))
    beam_reflector = BeamReflector(start_beam, puzzle_input_array)
    beam_reflector.reflect_all_beams()
    return len(set(b.coordinates for b in beam_reflector.seen_beams)) - 1


def test_main__example():
    # GIVEN the puzzle input from example
    # WHEN the function is called
    # THEN output from the example is returned
    assert main("example.txt") == 46


output = main("exercise.txt")
