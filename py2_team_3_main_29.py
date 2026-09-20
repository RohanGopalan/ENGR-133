"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     14.2.3 Py2 Team 3 main
    Team ID:        LC2 - 29
    Author:         Rohan Gopalan, gopalanr@purdue.edu
    Date:           09/18/2026

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

import py2_team_3_escape_velocity_29 as ev
import py2_team_3_mass_29 as mass
import py2_team_3_volume_29 as volume


def main():

    # initialize the gravitational constant
    G = 6.67430e-11

    # get user input for density and radius
    rho = float(input("Enter the average density of the planet: "))
    radius = float(input("Enter the radius of the planet: "))

    # calculate volume, mass, and escape velocity
    vol = volume.calc_volume(radius)
    m = mass.calc_mass(rho, vol)
    escapevelo = ev.calc_escape_velocity(G, m, radius)

    # convert radius to km
    radius /= 1000

    # print results

    print(
        f"For a planet with radius {radius:,.1f} km and density {rho:,.2f} kg/m^3, the estimated escape velocity is {escapevelo:,.2f} m/s"
    )


if __name__ == "__main__":
    main()
