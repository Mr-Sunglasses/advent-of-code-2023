import os
import re
from typing import Union, List


TO_DIGITS = {"one": "1", "two": "2", "three": "3", "four": "4",
             "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

NUMBERS_RE = re.compile("(one|two|three|four|five|six|seven|eight|nine)")


def resolve_spelling(lines: list[str]):
    for i in range(len(lines)):
        lines[i] = NUMBERS_RE.sub(
            lambda m: TO_DIGITS.get(m.group(0)), lines[i])


def sum_finded_calibrated_values(problem_file_path: Union[str, os.PathLike]) -> int:
    with open(problem_file_path) as f:
        CONST_LIST_VALUES: List[str] = f.readlines()
        # filter the list
        CONST_LIST_VALUES = [x.strip("\n") for x in CONST_LIST_VALUES]

    resolve_spelling(CONST_LIST_VALUES)
    EXTRACTED_CALIBRATION_VALUES: List[str] = []

    for i in CONST_LIST_VALUES:
        extracted_numbers: str = re.findall("[0-9]", i)
        if len(extracted_numbers) > 1:
            final_value: str = extracted_numbers[0] + extracted_numbers[-1]
            EXTRACTED_CALIBRATION_VALUES.append(final_value)
        elif len(extracted_numbers) == 1:
            final_value: str = extracted_numbers[0] + extracted_numbers[0]
            EXTRACTED_CALIBRATION_VALUES.append(final_value)
        else:
            final_value: str = ""
            EXTRACTED_CALIBRATION_VALUES.append(final_value)

    return sum([int(i) for i in EXTRACTED_CALIBRATION_VALUES])


print(sum_finded_calibrated_values(problem_file_path="case.txt"))
