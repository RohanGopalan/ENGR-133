"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     Py2 Ind 2 functions
    Team ID:        LC2 - 29
    Author:         Rohan Gopalan, gopalanr@purdue.edu
    Date:           9/22/2026

Contributors:

    My contributor(s) helped me:
    [X] understand the assignment expectations without
        telling me how they will approach it.
    [X] understand different ways to think about a solution
        without helping me plan my solution.
    [X] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

from math import pi

GALLONS_PER_FEET_CUBED = 576 / 77


def main():
    pass


def standard(len_1, len_2, dep_s, dep_d):
    if len_1 > 0 and len_2 > 0 and dep_s > 0 and dep_d > 0:

        # find the area of the flat face of the pool
        area = (dep_d - dep_s) * (1 / 3 * len_1)
        area += len_1 * dep_s

        # find volume by multiply area by length 2
        volume = area * len_2

        return volume * GALLONS_PER_FEET_CUBED
    else:
        print("Please enter valid dimensions.")
        return None


def round(len_1, len_2, dep_s, dep_d):
    if len_1 > 0 and len_2 > 0 and dep_s > 0 and dep_d > 0:

        # find volume of frustum (bottom curved ramp part)
        vol_frustum = (
            pi / 3 * (dep_d - dep_s) * (len_1 * len_1 + len_1 * len_2 + len_2 * len_2)
        )

        # find volume of top cylinder
        vol_cyl = pi * len_1 * len_1 * dep_s

        # add to get total volume and return
        return (vol_frustum + vol_cyl) * GALLONS_PER_FEET_CUBED

    else:
        print("Please enter valid dimensions.")
        return None


def ramp(len_1, len_2, dep_s, dep_d):
    if len_1 > 0 and len_2 > 0 and dep_s > 0 and dep_d > 0:

        # find area of ramp face
        area = (len_1 / 6) * (dep_s + dep_d)
        area += (1 / 2) * (len_1) * (dep_s)

        # multiply by len_2 to get volume
        volume = area * len_2

        return volume * GALLONS_PER_FEET_CUBED
    else:
        print("Please enter valid dimensions.")
        return None


if __name__ == "__main__":
    main()
