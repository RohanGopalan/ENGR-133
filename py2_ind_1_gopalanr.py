"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     Py2 Ind 1
    Team ID:        LC2 - 29
    Author:         Rohan Gopalan, gopalanr@purdue.edu
    Date:           e.g. 01/23/2026

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

import sys

CRITICAL_TEMP = 304.2
CRITICAL_PRESSURE = 73.8

MAX_OPERATING_TEMP = 344.14
MAX_OPERATING_PRESSURE = 137


def main():

    # inputs for temperature and float and checking for validity
    temp = float(input("Enter the temperature of carbon dioxide in Kelvin: "))
    if temp < 0:
        sys.exit("Error: Please enter a valid temperature.")

    pressure = float(input("Enter the pressure of carbon dioxide in bar: "))
    if pressure < 0:
        sys.exit("Error: Please enter a valid pressure.")

    # check_status call
    check_status(temp, pressure)


def check_status(temp, pressure):

    # initialize booleans for checking the critical point
    temp_at_critical = False
    pressure_at_critical = False

    # conditions checking for temperature
    if temp < CRITICAL_TEMP:
        print("CO2 is below the critical temperature.")
        increase_by = CRITICAL_TEMP - temp
        print(f"Increase the temperature by at least {increase_by:.2f} Kelvin.")

    elif temp == CRITICAL_TEMP:
        temp_at_critical = True

    elif temp >= 0.95 * MAX_OPERATING_TEMP:
        print("Warning! Reduce the temperature!")
        decrease_by = temp - (0.95 * MAX_OPERATING_TEMP)
        print(f"Decrease the temperature by at least {decrease_by:.2f} Kelvin.")

    else:
        print("Temperature is within safe operating conditions.")

    # conditions checking for pressure
    if pressure < CRITICAL_PRESSURE:
        print("CO2 is below the critical pressure.")
        increase_by = CRITICAL_PRESSURE - pressure
        print(f"Increase the pressure by at least {increase_by:.2f} bar.")

    elif pressure == CRITICAL_PRESSURE:
        pressure_at_critical = True

    elif pressure >= 0.95 * MAX_OPERATING_PRESSURE:
        print("Warning! Reduce the pressure!")
        decrease_by = pressure - (0.95 * MAX_OPERATING_PRESSURE)
        print(f"Decrease the pressure by at least {decrease_by:.2f} bar.")

    else:
        print("Pressure is within safe operating conditions.")

    # checking for critical point
    if temp_at_critical and pressure_at_critical:
        print("CO2 is at the critical point.")


if __name__ == "__main__":
    main()
