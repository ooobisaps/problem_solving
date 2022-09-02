#!/bin/python3
import sys


def split(name):
    left, right, parsed_name = 0, 1, ""

    while right < len(name):
        if name[right].isupper():
            parsed_name += name[left:right].lower() + " "
            left = right

        right += 1

    return parsed_name + name[left:].lower()


def combine(name, entity):
    parts = name.split()
    parsed_name = parts[0]
    for i in range(1, len(parts)):
        parsed_name += parts[i].capitalize()

    if entity == "M":
        parsed_name += "()"

    if entity == "C":
        parsed_name = parsed_name[0].upper() + parsed_name[1:]

    return parsed_name


def camelCase4(s):
    action, entity, name = s.split(";")

    if action == "C":
        parsed_name = combine(name, entity)

    if action == "S":
        parsed_name = split(name.replace("()", ""))

    return parsed_name


if __name__ == '__main__':
    for line in sys.stdin.read().splitlines():
        print(camelCase4(line.strip()))
