# PART 1:
def part_one(inp):
    pass


# PART 2:
def part_two(inp):
    pass

# PART 3:
def part_three(inp):
    pass


def main():
    data = []

    with open("input.txt", "r") as file:
        data = file.read().split("\n")

    print("Part 1:", part_one(data))
    # print("Part 2:", part_two(data))
    # print("Part 3:", part_three(data))


if __name__ == "__main__":
    main()
