"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Uses several nested loops to build and print several values with a matrix

Assignment Information:
    Assignment:     Py3 Pre 0
    Team ID:        LC2 - 29
    Author:         Rohan Gopalan, gopalanr@purdue.edu
    Date:           9/19/2026

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


def main():

    # First set of inputs
    print("Enter Matrix Dimensions")

    rows = int(input("Enter rows: "))
    columns = int(input("Enter columns: "))

    # Prints matrix using for loop
    matrix = build_matrix(rows, columns)
    traverse_with_for(matrix)

    print()
    print("Enter Matrix Dimensions")

    # second set of inputs
    rows = int(input("Enter rows: "))
    columns = int(input("Enter columns: "))
    stop = int(input("Enter Stop Value: "))

    # prints second matrix until stopping value
    matrix = build_matrix(rows, columns)
    traverse_with_while(matrix, stop)


# builds matrix numbered up from 1 in row-major order using a for loop
def build_matrix(rows, cols):

    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    num = 1

    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = num
            num += 1

    return matrix


# prints all values of a matrix using a for loop
def traverse_with_for(x):
    print("FOR loop traversal:")

    for row in range(len(x)):
        for col in range(len(x[row])):
            print(f"X[{row},{col}] = {x[row][col]}")


# prints values of a matrix until a stopping value using a while loop
def traverse_with_while(x, stop):
    print("WHILE loop traversal:")
    row = col = 0

    while row < len(x):

        while col < len(x[row]) and x[row][col] < stop:

            print(f"X[{row},{col}] = {x[row][col]}")
            col += 1

        row += 1
        col = 0


if __name__ == "__main__":
    main()
