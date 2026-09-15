"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Inputs value for first capacitor, initializes second capacitor to e^3 * sqrt(5), then computes parallel and series capacitance, then displays it.

Assignment Information:
    Assignment:     Py1 Ind 2
    Team ID:        LC2 - 04
    Author:         Rohan Gopalan, gopalanr@purdue.edu
    Date:           e.g. 09/13/2026

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

from math import e, sqrt

def main():
    # get values for both capacitor values
    c1 = float(input("Input the capacitance of the first capacitor [\u03bcF]: "))
    c2 = e**3 * sqrt(5)

    # calculate parallel and series capacitance
    parallel = c1 + c2
    series = 1 / (1 / c1 + 1 / c2)

    # display the results in a table format
    # didn't use 10.2f because I couldn't get the spacing to work properly, so I did it manually
    print(f"{'Type':<15}{'First':<11}{'Second':<12}{'Total'}")
    print(f"{'Series':<13}{c1:.1f} μF     {c2:.1f} μF     {series:.1f} μF")
    print(f"{'Parallel':<13}{c1:.1f} μF     {c2:.1f} μF     {parallel:.1f} μF")


if __name__ == "__main__":
    main()
