"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     Py3 Team 3 b
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

from math import exp


def main():
    # get inputs for x and threshold
    x = float(input("Enter the value of x: "))
    error_thres = float(input("Enter the target error threshold: "))

    # assign returned values to # of terms and approximation
    terms, approx = estimate_with_thres(x, error_thres)

    # print outputs
    print(f"Terms needed: {terms}")
    print(f"Actual value: {exp(x):.2f}")
    print(f"Approximate value: {approx:.2f}")
    print(f"Target error threshold: {error_thres:.1f}%")


def estimate_with_thres(x, thres):

    # initialize all variables
    n = 0
    terms = 0
    approx = 0
    error = thres + 1

    # keep adding more terms until error is under the threshold
    while error > thres:

        # increment terms
        terms += 1

        # add one approximation term and find % error
        approx += x**n / my_factorial(n)
        error = abs((approx - exp(x)) / exp(x)) * 100

        # increment n then start next loop
        n += 1

    # return terms and approx
    return (
        terms,
        approx,
    )


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


if __name__ == "__main__":
    main()
