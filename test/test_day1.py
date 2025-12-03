from src.day1 import day_one


def test_day_one_part_one():
    with open(r"C:\Storage\Programming\AdventOfCode2025\data_test\day1_test.txt", "r", encoding="utf-8") as f:
        in_data = f.read().splitlines()

    expected = 3
    actual = day_one(in_data)[0]

    assert expected == actual


def test_day_one_part_two():
    with open(r"C:\Storage\Programming\AdventOfCode2025\data_test\day1_test.txt", "r", encoding="utf-8") as f:
        in_data = f.read().splitlines()

    expected = 6
    actual = day_one(in_data)[1]

    assert expected == actual
