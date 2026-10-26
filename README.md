# f1_telemetry_projects
A couple of codes for handling F1 telemetry data and analysing it.

There will be 4 projects in this repository eventually, those being the following:
  - 1D lap simulator for a straight
  - Simplified 2D lap simulator for a track of choice (current: N/A)
  - Brake analysis using F1 telemetry data
  - Simple thermodynamic tyre model

# Project 1
This project is a simple 1D lap simulator for a singualar 1000m straight
In the code, it is assumed that you will exit the corner before the straight at roughly 60 km/h, and will calculate your time and speed over the 1000m after you have inputted your weight, the weight of the car you are driving, and the power of the engine of said car.
Once the variables have been decided by you, the code will give you 3 things: the time it took to drive that straight, the speed at which you ended the straight and a visual representation of this through a graph of 'Velocity vs Distance' and 'Cumulative time vs Distance'
