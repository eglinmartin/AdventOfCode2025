
def day_two(data):
    count_one = 0
    count_two = 0

    data_split = data.split(',')
    for range_str in data_split:
        start_int = str(range_str.split('-')[0])
        end_int = str(range_str.split('-')[1])

        for num in range(int(start_int), int(end_int) + 1):
            num_string = str(num)
            num_length = len(num_string)

            # Part one - check for a single duplication between two halves of each number
            if num_length % 2 == 0:
                factor = num_length // 2
                factor_chunk = num_string[:factor]
                extrapolated_number = ''.join([factor_chunk] * int(num_length / factor))

                if int(extrapolated_number) == num:
                    print(num, factor, factor_chunk, extrapolated_number)
                    count_one += num

            # Part two - create list of all factors of each number and check each possible set of duplications
            factors_all = [i for i in range(1, num_length + 1) if num_length % i == 0]
            for factor in factors_all:
                if factor != num_length:
                    factor_chunk = num_string[:factor]
                    extrapolated_number = ''.join([factor_chunk] * int(num_length / factor))

                    if int(extrapolated_number) == num:
                        count_two += num
                        break

    return count_one, count_two


if __name__ == '__main__':
    in_data = r"C:\Storage\Programming\AdventOfCode2025\data\day2.txt"
    with open(in_data, "r", encoding="utf-8") as f:
        DATA = f.read().splitlines()

    part_one, part_two = day_two(DATA[0])
    print(part_one, part_two)
