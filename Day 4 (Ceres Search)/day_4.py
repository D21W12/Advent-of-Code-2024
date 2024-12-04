from itertools import count

import numpy as np
import re


def parse_puzzle_input(filename: str = "puzzle_input.txt") -> np.ndarray:
    file = open(filename, "r").read().splitlines()
    grid = []
    for i, line in enumerate(file):
        grid.append([])
        for char in line:
            grid[i].append(char)
    grid = np.array(grid)
    print(grid)
    return grid


def count_xmas(strings: list[str]) -> int:
    total = 0

    # Looping through all strings and counting the number of occurrences
    # of the substring XMAS and SAMX (XMAS inverted)
    for string in strings:
        total += len(re.findall("XMAS", string))
        total += len(re.findall("SAMX", string))

    return total


def part1(grid: np.ndarray) -> int:
    grid90 = np.rot90(grid)
    grid180 = grid[:,::-1]
    total = 0

    # Saving all rows and columns as strings in a list
    horizontal = ["".join(row) for row in grid]  # get list of row strings
    vertical = ["".join(column) for column in grid90]  # get list of column strings

    # Saving all diagonals as strings
    diagonals = ["".join(grid.diagonal(offset=i)) for i in range(-(grid.shape[0] - 1), grid.shape[1])]
    diagonals += ["".join(grid180.diagonal(offset=i)) for i in range(-(grid180.shape[0] - 1), grid180.shape[1])]

    # Summing up all the occurrences from the rows, columns, and diagonals
    total += count_xmas(horizontal)
    total += count_xmas(vertical)
    total += count_xmas(diagonals)

    return total


def part2(grid: np.ndarray) -> int:
    letters = {"M", "A", "S"}
    total = 0

    # Looping through every possible center of an X-MAS
    for i in range(1, grid.shape[0] - 1):
        for j in range(1, grid.shape[1] - 1):
            if grid[i,j] == "A":
                square = grid[i-1:i+2, j-1:j+2]
                diag1 = square.diagonal()
                diag2 = square[:,::-1].diagonal()
                if set(diag1) == letters and set(diag2) == letters:
                    total += 1

    return total


if __name__ == "__main__":
    grid = parse_puzzle_input()
    part1, part2 = part1(grid), part2(grid)
    print(f"The answer of part 1 is: {part1}")
    print(f"The answer of part 2 is: {part2}")
