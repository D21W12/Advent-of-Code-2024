import re


def parse_puzzle_input(filename: str = "puzzle_input.txt") -> str:
    memory = open(filename, "r").readlines()
    memory = "".join(memory)
    return memory


def part1(memory: str):
    total = 0
    muls = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", memory)
    for mul in muls:
        mul = mul.lstrip("mul(").rstrip(")")
        pre, post = mul.split(",")
        total += int(pre) * int(post)
    return total


def part2(memory: str):
    active = True
    filtered = ""
    for i in range(len(memory)):
        if memory[i:].startswith("do()"):
            active = True
        elif memory[i:].startswith("don't()"):
            active = False
        if active:
            filtered += memory[i]

    # Calling part1(), as we can re-use this logic to process our filtered memory
    return part1(filtered)


if __name__ == "__main__":
    memory = parse_puzzle_input()
    part1, part2 = part1(memory), part2(memory)
    print(f"The answer of part 1 is: {part1}")
    print(f"The answer of part 2 is: {part2}")
