"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Initializes three variables and calculates three equations using those variables, printing the results rounded to three decimal places.

Assignment Information:
    Assignment:     13.2.1 Py1 Team 1
    Team ID:        LC2 - 29
    Author:         Rohan Gopalan, gopalanr@purdue.edu
    Date:           9/3/2026

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

import math

def main():

    # initialize a, b, and c variables
    a = 101
    b = 7
    c = 12.34


    # calculate the first equation and print its result rounded to 3 decimal places
    firstCalc = (c*c) - (math.sin(b)*math.sin(b))
    print (f"equation 1: {firstCalc:.3f}")

    # calculate the second equation and print its result rounded to 3 decimal places
    secondCalc = (math.factorial(b) * (math.cos(math.pi/c) - a))
    print (f"equation 2: {secondCalc:.3f}")

    # calculate the third equation and print its result rounded to 3 decimal places
    thirdCalc = ( (c ** (math.pi * math.e)) * math.asin(math.sqrt(3)/2) ) / ( (a ** math.e) * b)
    print (f"equation 3: {thirdCalc:.3f}")

if __name__ == "__main__":
    main()
