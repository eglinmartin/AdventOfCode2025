
def day_one(data, val=50):
    count_one = 0
    count_two = 0

    for line in data:
        turn_number = int(line[1:])
        for i in range(turn_number):

            # Turn left (subtract 1 from val n times)
            if line[0] == 'L':
                val -= 1

            # Turn left (add 1 to val n times)
            elif line[0] == 'R':
                val += 1

            # Check if current val divisible by 100 (dial on zero)
            if val % 100 == 0:
                count_two += 1

        # Check if current val divisible by 100 (dial on zero)
        if val % 100 == 0:
            count_one += 1

    return count_one, count_two


if __name__ == '__main__':
    in_data = r"C:\Storage\Programming\AdventOfCode2025\data\day1.txt"
    with open(in_data, "r", encoding="utf-8") as f:
        IN_DATA = f.read().splitlines()

    part_one, part_two = day_one(IN_DATA)
    print(part_one, part_two)
