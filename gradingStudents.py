#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    new_grade = []
    if len(grades) >= 1 and len(grades)<=60:
        for i in range(len(grades)):
            if grades[i] >=0 and grades[i] <= 100:
                if grades[i] < 38 :
                    new_grade.append(grades[i])
                else:
                    round = 5 - (grades[i]%5)
                    if round < 3 and round > 0:
                        grades[i]+= round
                        new_grade.append(grades[i])
                    else:
                        new_grade.append(grades[i])
            else:
                new_grade.append(grades[i])
    return new_grade
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
