from src.day5 import day_five


def test_day_five_part_one():
    with open(r"C:\Repos\Personal\AdventOfCode2025\data_test\day5_test.txt", "r", encoding="utf-8") as f:
        in_data = f.read().splitlines()

    expected = 3
    actual = day_five(in_data)[0]

    assert actual == expected


def test_day_five_part_two():
    with open(r"C:\Repos\Personal\AdventOfCode2025\data_test\day5_test.txt", "r", encoding="utf-8") as f:
        in_data = f.read().splitlines()

    expected = 14
    actual = day_five(in_data)[1]

    assert actual == expected
