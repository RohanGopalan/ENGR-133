"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Uses several nested loops to build and print several values with a matrix

Assignment Information:
    Assignment:     Py3 Team 2
    Team ID:        LC2 - 29
    Author:         Rohan Gopalan, gopalanr@purdue.edu
    Date:           9/22/2026

Contributors:
    Zachary Yona, zyona@purdue.edu
    Anay Guturi, aguturi@purdue.edu
    Skyler Wenger, wenger21@purdue.edu
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


def factorial(n):
    if n == 1:
        # We've hit the bottom of the recursion! RETREAT!
        return n
    elif n == 0:
        # Special case: Return 1 for 0
        return 1
    else:
        # We use recursion because we're cool like that (and it's way simpler than a loop)
        return n * factorial(n - 1)


def main():

    # prompt user to input a number
    num = int(input("Enter a number: "))

    # first, check for valid inputs
    # then initiate the recursive factorial function and print the result
    if num < 0:
        print("Error -999 [Negative Input]")
    else:
        facted = factorial(num)
        print(f"The Factorial of {num} is {facted}.")


if __name__ == "__main__":
    main()
