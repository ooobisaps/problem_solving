#!/bin/python3
import os


def timeConversion(s):
    hour, minute, second_with_midday_check = s.split(':')
    second, is_midday = second_with_midday_check[:2], second_with_midday_check[2:]

    if is_midday == "AM" and int(hour) == 12:
        hour = "00"
    if is_midday == "PM" and int(hour) < 12:
        hour = int(hour) + 12

    return f"{hour}:{minute}:{second}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = timeConversion(s)

    fptr.write(result + '\n')
    fptr.close()
