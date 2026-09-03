"""
Course Number: ENGR 13300
Semester: Spring 2026

Description:
    This program initializes a, b, and c, then uses several functions to perform
    a calculation and print the result.

Assignment Information:
    Assignment:     Py1 Pre-class 0
    Team ID:        LC2 - 04
    Author:         Rohan Gopalan, gopalanr@purdue.edu
    Date:           9/3/2026

Contributors:

    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
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

def main():
    a = 101
    b = 7
    c = 12.34

    firstCalc = (c*c) - (math.sin(b)*math.sin(b))
    print (f"Equation 1: {firstCalc:.3f}")

    secondCalc = (math.factorial(b) * (math.cos(math.pi/c) - a))
    print (f"Equation 2: {secondCalc:.3f}")

    thirdCalc = ( (c ** (math.pi * math.e)) * math.asin(math.sqrt(3)/2) ) / ( (a ** math.e) * b)
    print (f"Equation 3: {thirdCalc:.3f}")

if __name__ == "__main__":
    main()
