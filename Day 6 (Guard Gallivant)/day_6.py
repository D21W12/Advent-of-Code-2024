import numpy as np


def parse_puzzle_input(filename: str = "puzzle_input.txt") -> (np.ndarray, (int, int)):
    file = open(filename, "r").read().splitlines()
    grid = []

    # Looping through every line of the file
    for i, line in enumerate(file):

        row = []  # This list will represent the rows of the grid
        for j, char in enumerate(line):

            # Checking if the position is the starting position
            if char == "^":

                # Saving the starting position of the guard as a numpy array [row, col]
                start = np.array([i, j])

            row.append(char)  # Appending the char to the row

        grid.append(row)

    grid = np.array(grid)  # Casting the 2D list to a numpy array
    return grid, start


def part1(grid: np.ndarray[str], pos: np.ndarray[int]) -> int:
    total = 1  # Initialize with 1 to include starting position
    height, width = grid.shape
    dir_ = np.array([-1, 0])  # Current direction

    # Boolean array storing if a position has already been visited
    visited = np.zeros(shape=(height, width), dtype=bool)

    while 0 <= (pos[0] + dir_[0]) < height and 0 <= (pos[1] + dir_[1]) < width:
        visited[pos[0], pos[1]] = True

        # Changing the direction until there is no more obstacle in front
        while grid[pos[0] + dir_[0], pos[1] + dir_[1]] == "#":
            dir_[0], dir_[1] = dir_[1], -dir_[0]
        pos += dir_

        # Count the distinct positions
        if not visited[pos[0], pos[1]]:
            total += 1

    return total


def part2(grid: np.ndarray[str], start: (int, int)):
    pass


if __name__ == "__main__":
    grid, start = parse_puzzle_input()
    part1, part2 = part1(grid, start), part2(grid, start)
    print(f"The answer of part 1 is: {part1}")
    print(f"The answer of part 2 is: {part2}")
