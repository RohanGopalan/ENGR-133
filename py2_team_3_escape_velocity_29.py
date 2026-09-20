"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Calculates the escape velocity

Assignment Information:
    Assignment:     14.2.3 Py2 Team 3 escape velocity
    Team ID:        LC2 - 29
    Author:         Zachary Yona, zyona@purdue.edu
                    Rohan Gopalan, gopalanr@purdue.edu
                    Skyler Wenger, wenger21@purdue.edu
                    Anay Guturi, aguturi@purdue.edu
    Date:           09/17/2026

Contributors:
    Name, login@purdue [repeat for each]

    My contributor(s) helped me:
    [x] understand the assignment expectations without
        telling me how they will approach it.
    [x] understand different ways to think about a solution
        without helping me plan my solution.
    [x] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

import math


def calc_escape_velocity(G, mass, radius):
    # Toss bad inputs
    if radius <= 0:
        print("Radius must be greater than zero!")
        return 0
    elif mass <= 0:
        print("Mass must be greater than zero!")
        return 0
    # We don't need an explicit else block here, since the function returns on both previous statements.
    v_e = math.sqrt((2 * G * mass) / radius)
    return v_e


def main():
    # nothing here, just using the function above
    pass


if __name__ == "__main__":
    main()
