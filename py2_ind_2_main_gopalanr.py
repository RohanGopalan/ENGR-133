"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     Py2 Ind 2 main
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

import py2_ind_2_functions_gopalanr as funcs


def main():

    # get input for pool type and check validity
    pool_name = input(
        "Enter the name of the pool to calculate (Standard, Ramp, or Round): "
    )
    pool_name = pool_name.lower()
    if not (pool_name == "standard" or pool_name == "round" or pool_name == "ramp"):
        print("Please run the program again and enter a valid pool name.")

    else:
        # get inputs for all dimensions of the pool
        l1 = int(input("Enter the surface length or radius. "))
        l2 = int(input("Enter the surface width or bottom radius. "))
        ds = int(input("Enter the shallow end depth. "))
        dd = int(input("Enter the deep end depth. "))

        # calculate volume based on pool type given the dimensions
        if pool_name == "standard":
            volume = funcs.standard(l1, l2, ds, dd)
        elif pool_name == "ramp":
            volume = funcs.ramp(l1, l2, ds, dd)
        elif pool_name == "round":
            volume = funcs.round(l1, l2, ds, dd)

        # print volume that is returned from the functions
        pool_name = pool_name.capitalize()
        print(
            f"The volume of the {pool_name} pool with your dimensions is {volume:,.2f} gallons."
        )


if __name__ == "__main__":
    main()
