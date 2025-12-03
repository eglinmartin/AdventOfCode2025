from src.day2 import day_two


def test_day_two_part_one():
    with open(r"C:\Storage\Programming\AdventOfCode2025\data_test\day2_test.txt", "r", encoding="utf-8") as f:
        in_data = f.read().splitlines()

    expected = 1227775554
    actual = day_two(in_data[0])[0]

    assert expected == actual


def test_day_two_part_two():
    with open(r"C:\Storage\Programming\AdventOfCode2025\data_test\day2_test.txt", "r", encoding="utf-8") as f:
        in_data = f.read().splitlines()

    expected = 4174379265
    actual = day_two(in_data[0])[1]

    assert expected == actual
