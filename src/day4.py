
def get_paper_rolls(data):
    count = 0
    rolls_to_remove = []

    for i, row in enumerate(data):
        for j, col in enumerate(row):
            num_rows = len(data)
            num_cols = len(row)

            directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
            adjacent_tiles = [(i+dir_val[0], j+dir_val[1]) for dir_val in directions]

            adjacent_tiles_filtered = [tile_set for tile_set in adjacent_tiles if 0 <= tile_set[0] < num_rows and 0 <= tile_set[1] < num_cols]
            num_adjacent = [tile_set for tile_set in adjacent_tiles_filtered if data[tile_set[0]][tile_set[1]] == '@']

            if data[i][j] == '@' and len(num_adjacent) < 4:
                count += 1
                rolls_to_remove.append([i, j])

    for index in rolls_to_remove:
        data[index[0]][index[1]] = 'x'

    return count


def day_four(data):
    count_one = 0
    count_two = 0

    data_one = [list(line) for line in data]
    num_rolls = get_paper_rolls(data_one)
    count_one += num_rolls

    data_two = [list(line) for line in data]
    while True:
        num_rolls = get_paper_rolls(data_two)
        count_two += num_rolls
        if num_rolls <= 0:
            break

    return count_one, count_two


if __name__ == '__main__':
    in_data = r"C:\Repos\Personal\AdventOfCode2025\data\day4.txt"
    with open(in_data, "r", encoding="utf-8") as f:
        DATA = f.read().splitlines()

    part_one, part_two = day_four(DATA)
    print(part_one, part_two)
