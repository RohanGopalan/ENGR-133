"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     Py3 Team 3 a
    Team ID:        LC2 - 29
    Author:         Rohan Gopalan, gopalanr@purdue.edu
                    Zachary Yona, zyona@purdue.edu
                    Anay Guturi, aguturi@purdue.edu
                    Skyler Wenger, wenger21@purdue.edu
    Date:           9/24/2026

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


def my_factorial(n):
    # check for valid inputs
    if n < 0:
        return -999
    elif n == 1:
        # We've hit the bottom of the recursion! RETREAT!
        return n
    elif n == 0:
        # Special case: Return 1 for 0
        return 1
    else:
        # We use recursion because we're cool like that (and it's way simpler than a loop)
        return n * my_factorial(n - 1)


def main():
    # Get inputs
    n = int(input("Enter the value of n: "))
    x = float(input("Enter the value of x: "))

    # Calculate the actual value of e^x
    actual = math.e**x

    # Run the Maclaurin series with n terms
    estimate = 0
    # The bounds are a tad funky, because we actually want to include the nth term.
    for m in range(0, n + 1):
        # The mth term in the Maclaurin series equals (x^m)/m!, which is calculated below and then added to our estimate
        current_term = (x**m) / my_factorial(m)
        estimate += current_term

    # Calculate our percent error
    percent_error = 100 * (estimate - actual) / actual

    # Output! (Not factorial)
    print(f"Actual value: {actual:.2f}")
    print(f"Approximate value: {estimate:.2f}")
    print(f"Error: {percent_error:.1f}%")


if __name__ == "__main__":
    main()
