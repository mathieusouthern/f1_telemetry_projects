import numpy as np
import matplotlib.pyplot as plt

# ===================================
#   Section 1: Car data
# ===================================
print("How much do you weigh (in kg)?")
driver_mass = float(input('> '))

print("What is the mass of the car (in kg)?")
car_mass = float(input('> '))

print("What is the maximum power of the car (in Watts)?")
power = float(input('> '))


mass = driver_mass + car_mass  # combined mass of driver and car
max_power = power  # maximum power of the car
rho = 1.225  # Air density
c_da = 1.30  # Drag coeff
tyre_grip_limit = 2.0

# ===================================
#   Section 2: Track Environment
# ===================================
track_length = 1000.0  # metres
dx = 1.0
distances = np.arange(0, track_length, dx)
velocities = np.zeros(len(distances))
time_elapsed = np.zeros(len(distances))

# Set intial conditions: Exiting a slow corner into a straight at 60km/h (16.67 m/s)
velocities[0] = 16.67
time_elapsed[0] = 0.0

# ===================================
#   Section 3: Numerical Integration Loop
# ===================================
print("Simulating 1D Longitudinal Acceleration Profile...")

for i in range(0, len(distances) - 1):
    v_current = velocities[i]

    f_drag = 0.5 * rho * c_da * (v_current**2)  # aero drag force

    # Calculate Physical traction limit
    f_engine_ideal = max_power * 1/max(v_current, 1.0)

    # Physical traction limit, the tyres can only exert so much force on the tarmac
    f_tyre_max = tyre_grip_limit * mass * 9.81
    f_engine = min(f_engine_ideal, f_tyre_max)

    f_net = f_engine - f_drag  # Net tractive force acting on the vehicle chassis

    a = f_net / mass  # acceleration

    # update next segemtns velocity with equation of motion
    velocities[i+1] = np.sqrt(max(v_current**2 + 2*a*dx, 0.1))

    v_avg = (v_current + velocities[i+1]) / 2.0
    dt = dx / v_avg
    time_elapsed[i+1] = time_elapsed[i] + dt

total_time = time_elapsed[-1]
top_speed_kmh = velocities[-1] * 3.6
print(
    f"Simulation complete! Time down straight: {total_time:.3f} seconds. Exit speed: {top_speed_kmh:.1f} km/h")

# ===================================
#   Section 4:Performance Visual Plot
# ===================================
fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'cyan'
ax1.set_xlabel('Distance along straight', fontsize=12)
ax1.set_ylabel('Velocity (km/h)', color=color, fontsize=12)
ax1.plot(distances, velocities * 3.6, color=color,
         linewidth=2.5, label='Car Speed')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, alpha=0.2)

ax2 = ax1.twinx()
color = 'gold'
ax2.set_ylabel('Cumulative Time (Seconds)', color=color, fontsize=12)
ax2.plot(distances, time_elapsed, color=color,
         linestyle='--', linewidth=2, label='Time Elapsed')

plt.title('formula 1 Performance Simulation: 1D Lap Time Simulator',
          fontsize=14, pad=15)
fig.tight_layout()
plt.legend()
plt.show()
