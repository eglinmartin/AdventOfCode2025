
def get_values(values_list, data_line_values, i, num_revisions):
    if i == 0:
        data_line_values_cut = data_line_values[:-(num_revisions - i - 1)]
        num = sorted(data_line_values_cut, key=lambda x: (-x[0], x[1]))[0]

    elif i == num_revisions - 1:
        cut_value = values_list[i - 1][1] + 1
        data_line_values_cut = data_line_values[cut_value:]
        num = sorted(data_line_values_cut, key=lambda x: (-x[0], x[1]))[0]

    else:
        cut_value = values_list[i - 1][1] + 1
        data_line_values_cut = data_line_values[cut_value:-(num_revisions - i - 1)]
        num = sorted(data_line_values_cut, key=lambda x: (-x[0], x[1]))[0]

    return num


def day_three(data):
    count_one = 0
    count_two = 0

    for data_line in data:
        data_line_values = [(int(num), i) for i, num in enumerate(data_line)]

        num_revisions = 2
        values_list = []
        for i in range(num_revisions):
            values_list.append(get_values(values_list, data_line_values, i, num_revisions))
        count_one += int(''.join(map(str, [i[0] for i in values_list])))

        num_revisions = 12
        values_list = []
        for i in range(num_revisions):
            values_list.append(get_values(values_list, data_line_values, i, num_revisions))
        count_two += int(''.join(map(str, [i[0] for i in values_list])))

    return count_one, count_two


if __name__ == '__main__':
    in_data = r"C:\Storage\Programming\AdventOfCode2025\data\day3.txt"
    with open(in_data, "r", encoding="utf-8") as f:
        DATA = f.read().splitlines()

    part_one, part_two = day_three(DATA)
    print(part_one, part_two)
