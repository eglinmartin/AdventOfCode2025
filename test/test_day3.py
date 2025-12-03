from src.day3 import day_three


def test_day_three_part_one():
    with open(r"C:\Storage\Programming\AdventOfCode2025\data_test\day3_test.txt", "r", encoding="utf-8") as f:
        in_data = f.read().splitlines()

    expected = 357
    actual = day_three(in_data)[0]

    assert actual == expected


def test_day_three_part_two():
    with open(r"C:\Storage\Programming\AdventOfCode2025\data_test\day3_test.txt", "r", encoding="utf-8") as f:
        in_data = f.read().splitlines()

    expected = 3121910778619
    actual = day_three(in_data)[1]

    assert actual == expected
