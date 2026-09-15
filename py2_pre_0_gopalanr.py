"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     Py2 Pre 0
    Team ID:        LC2 - 04
    Author:         Rohan Gopalan, gopalanr@purdue.edu
    Date:           09/11/2026

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
    # input and initialize variables

    a = float(input("Input a number for variable a: "))
    b = 135
    c = 3

    # call the calc_perform function
    result = calc_perform(a, b, c)
    print(f"The result of the function was {result:.2f}")

    

def calc_perform(a, b, c):
    # use the if statement to determine which equation to use based on the value of a
    if (a > 4):
        answer = (a*a + math.cos(b) - math.log(c)) / (b - (a * c))
    else:
        answer = (math.sqrt(a+b)) / (math.factorial(c) + math.sin(b))
    return answer

if __name__ == "__main__":
    main()
