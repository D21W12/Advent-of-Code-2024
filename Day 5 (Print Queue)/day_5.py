import numpy as np

def parse_puzzle_input(filename: str = "puzzle_input.txt") -> (list, list):
    file = open(filename, "r").read().splitlines()
    si = file.index("")  # Seperator index
    rules, updates = file[:si], file[si+1:]

    # Splitting and typecasting into integers
    rules = [[int(n) for n in rule.split("|")] for rule in rules]
    updates = [[int(n) for n in update.split(",")] for update in updates]
    return rules, updates


def is_correct(update: list[int], rules: list[list[int]]):
    for i, rule in enumerate(rules):
        if set(rule).issubset(set(update)):
            index_pre = update.index(rule[0])
            index_post = update.index(rule[1])

            # When a rule is not satisfied, go to the next update
            if index_pre > index_post:
                return False

        # If last rule is satisfied, the update is in the correct order
        if i == len(rules) - 1:
            return True


def part1(rules: list[list[int]], updates: list[list[int]]) -> int:
    total = 0

    # Checking every update
    for update in updates:

        # Checking if the update satisfies all rules
        if is_correct(update, rules):
            total += update[len(update)//2]


    return total


def part2(rules: list[list[int]], updates: list[list[int]]) -> None:
    total = 0

    for update in updates:
        if not is_correct(update, rules):
            non_trivial_rules = [rule for rule in rules if set(rule).issubset(set(update))]

            i = 0
            while i < len(non_trivial_rules) - 1:  # Only stop the loop once all rules are satisfied
                i = 0
                for rule in non_trivial_rules:
                    index_pre = update.index(rule[0])
                    index_post = update.index(rule[1])

                    # When a rule is not satisfied, move
                    if index_pre > index_post:
                        update.insert(index_post, update.pop(index_pre))
                    else:
                        i += 1

            total += update[len(update)//2]

    return total


if __name__ == "__main__":
    rules, updates = parse_puzzle_input()
    part1, part2 = part1(rules, updates), part2(rules, updates)
    print(f"The answer of part 1 is: {part1}")
    print(f"The answer of part 2 is: {part2}")
