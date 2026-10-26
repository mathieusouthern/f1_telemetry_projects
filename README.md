# F1 Telemetry Projects
Some code for handling F1 telemetry data and analysing it.

There will be 4 projects in this repository eventually, those being the following:
  - 1D lap simulator for a 1000m straight
  - Simplified 2D lap simulator for a track of choice (current: N/A)
  - Brake analysis using F1 telemetry data
  - Simple thermodynamic tyre model

# Project 1 - 1D Lap Simulator for a Straight
This project is a simple 1D lap simulator for a singualar 1000m straight.

In the code, it is assumed that you will exit the corner before the straight at roughly 60 km/h, and will calculate your time and speed over the 1000m after you have inputted your weight, the weight of the car you are driving, and the power of the engine of said car.

Once the variables have been decided by you, the code will give you 3 things: the time it took to drive that straight, the speed at which you ended the straight and a visual representation of this through a graph of 'Velocity vs Distance' and 'Cumulative time vs Distance'

For example, if you gave the following:
 - Mass = 70kg
 - Car mass = 750kg
 - Power = 800000W


You would get the following:

Simulating 1D Longitudinal Acceleration Profile...

Simulation complete! Time down straight: 12.749 seconds. Exit speed: 353.6 km/h
<img width="625" height="368" alt="image" src="https://github.com/user-attachments/assets/146d762e-7f99-4326-8f07-22a4f9b0bc15" />
