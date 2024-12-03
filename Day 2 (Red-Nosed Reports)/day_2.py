import numpy as np


def parse_puzzle_input(filename="puzzle_input.txt") -> list:
    file = open(filename, "r").read().splitlines()
    reports = [np.array(report.split(), dtype=int) for report in file]
    return reports


def safe(report: np.array) -> bool:
    distances = report[1:] - report[:-1]
    if not np.any(np.abs(distances) > 3):
        return np.sum(distances >= 0) == 0 or np.sum(distances <= 0) == 0
    return False


def part1(reports: list) -> int:
    safe_reports = 0
    for report in reports:
        safe_reports += safe(report)
    return safe_reports


def part2(reports: list) -> int:
    safe_reports = 0
    for report in reports:
        if safe(report):
            safe_reports += 1
            continue

        # This is the most ugly bruteforcing code I've written all year
        for i in range(report.size):
            report_copy = list(report.copy())
            report_copy.pop(i)
            report_copy = np.array(report_copy)
            if safe(report_copy):
                safe_reports += 1
                break

    return safe_reports


if __name__ == "__main__":
    reports = parse_puzzle_input()
    part1, part2 = part1(reports), part2(reports)
    print(f"The answer of part 1 is: {part1}")
    print(f"The answer of part 2 is: {part2}")
