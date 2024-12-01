import numpy as np


def parse_puzzle_input(filename="puzzle_input.txt") -> (np.ndarray[int], np.ndarray[int]):
    file = open(filename, "r").read().splitlines()
    left, right = [], []
    for line in file:
        numbers = line.split()
        ln, rn = int(numbers[0]), int(numbers[1])
        left.append(ln)
        right.append(rn)
    left = np.array(left, dtype=int)
    right = np.array(right, dtype=int)
    return left, right


def part1(left: np.ndarray[int], right: np.ndarray[int]) -> int:
    left.sort()
    right.sort()
    distances = np.abs(left - right)
    total_distance = np.sum(distances)
    return total_distance


def part2(left: np.ndarray[int], right: np.ndarray[int]) -> int:
    similarity_score = 0
    intersection = np.intersect1d(left, right)
    for id in intersection:
        similar = right == id
        similarity_score += id * np.sum(similar)
    return similarity_score


if __name__ == "__main__":
    left, right = parse_puzzle_input()
    part1, part2 = part1(left, right), part2(left, right)
    print(f"The answer of part 1 is: {part1}")
    print(f"The answer of part 2 is: {part2}")
