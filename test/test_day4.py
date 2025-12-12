from src.day4 import day_four


def test_day_four_part_one():
    with open(r"C:\Repos\Personal\AdventOfCode2025\data_test\day4_test.txt", "r", encoding="utf-8") as f:
        in_data = f.read().splitlines()

    expected = 13
    actual = day_four(in_data)[0]

    assert actual == expected


def test_day_four_part_two():
    with open(r"C:\Repos\Personal\AdventOfCode2025\data_test\day4_test.txt", "r", encoding="utf-8") as f:
        in_data = f.read().splitlines()

    expected = 43
    actual = day_four(in_data)[1]

    assert actual == expected
