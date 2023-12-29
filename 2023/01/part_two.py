import re
import typing as t

with open('input4.txt', 'r') as file:
    lines = file.readlines()

words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

digit_pattern = "|".join([r"\d", *words])
full_digits = re.compile(
    rf"^.*?(?>(?P<first>{digit_pattern}))(?>.*(?P<last>{digit_pattern}))?.*$",
    flags=re.MULTILINE,
)
digits = {d: int(d) for d in "123456789"} | words


def full_calibration_values(text: str) -> t.Iterator[int]:
    for match in full_digits.finditer(text):
        yield 10 * digits[match["first"]] + digits[match["last"] or match["first"]]


print(sum(full_calibration_values("".join(lines))))