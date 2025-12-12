from itertools import groupby


def day_five(data):
    count_one = 0
    count_two = 0

    data_lists = [list(group) for key, group in groupby(data, key=lambda x: x != "") if key]
    data_entries = [int(entry) for entry in data_lists[1]]
    data_ranges = [[int(range_entry.split('-')[0]), int(range_entry.split('-')[1])] for range_entry in data_lists[0]]

    # Part one
    for entry in data_entries:
        for range_tuple in data_ranges:
            if entry in range(range_tuple[0], range_tuple[1] + 1):
                count_one += 1
                break

    # Part two
    ranges_sorted = sorted(data_ranges, key=lambda x: x[0])
    fresh_ranges = []

    for data_range in ranges_sorted:
        if not fresh_ranges or data_range[0] > fresh_ranges[-1][1]:
            fresh_ranges.append(data_range)
        else:
            fresh_ranges[-1][1] = max(fresh_ranges[-1][1], data_range[1])
    count_two += sum(end - start + 1 for start, end in fresh_ranges)

    return count_one, count_two


if __name__ == '__main__':
    in_data = r"C:\Repos\Personal\AdventOfCode2025\data\day5.txt"
    with open(in_data, "r", encoding="utf-8") as f:
        DATA = f.read().splitlines()

    part_one, part_two = day_five(DATA)
    print(part_one, part_two)
