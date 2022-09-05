#!/bin/python3

import os


def gradingStudents(grades):
    final_grades = []
    for grade in grades:
        next_multiple_5 = grade + (5 - grade % 5)

        if next_multiple_5 - grade < 3 and next_multiple_5 >= 40:
            final_grades.append(next_multiple_5)
        else:
            final_grades.append(grade)
    
    return final_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
