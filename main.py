from vpython import *

# Create a list to store the spheres
spheres = []

# Set the gravitational constant
G = 6.67408e-11

# Set the mass and radius of the spheres
mass = 1.0
radius = 0.1

# Set the initial positions and velocities of the spheres
for i in range(100):
    # Generate random initial positions within a certain range
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    z = random.uniform(-10, 10)
    position = vector(x, y, z)

    # Generate random initial velocities within a certain range
    vx = random.uniform(-1, 1)
    vy = random.uniform(-1, 1)
    vz = random.uniform(-1, 1)
    velocity = vector(vx, vy, vz)

    # Create a sphere with the specified mass, radius, position, and velocity
    sphere = sphere(pos=position, radius=radius, mass=mass, v=velocity)

    # Add the sphere to the list
    spheres.append(sphere)

# Set the timestep and total time of the simulation
dt = 0.01
total_time = 10

# Set the scene properties
scene.autoscale = False
scene.range = 15

# Run the simulation for the specified total time
for t in range(int(total_time / dt)):
    # Update the positions and velocities of the spheres
    for i, sphere_i in enumerate(spheres):
        # Initialize the net force on the sphere to zero
        net_force = vector(0, 0, 0)

        # Calculate the gravitational force between the sphere and each other sphere
        for j, sphere_j in enumerate(spheres):
            # Skip the sphere if it is the same as the current sphere
            if i == j:
                continue

            # Calculate the distance between the two spheres
            r = sphere_j.pos - sphere_i.pos
            r_mag = mag(r)

            # Calculate the gravitational force
            force = G * sphere_i.mass * sphere_j.mass / r_mag**2 * norm(r)

            # Add the gravitational force to the net force on the sphere
            net_force += force

        # Update the velocity and position of the sphere using the net force
        sphere_i.v += net_force / sphere_i.mass * dt
        sphere_i.pos += sphere_i.v * dt

    # Update the scene
    rate(1 / dt)
