from controller import Robot

# Constants
time_step = 16
num_motors = 8  # Reduced from 12 to 8 for quadruped
num_states = 4  # Reduced states for quadruped gait

FRONT = +0.7
BACK = -0.7
HI = +0.02
LO = -0.02

motor_names = [
    "hip_motor_l0", "hip_motor_l1",  # Left legs
    "hip_motor_r0", "hip_motor_r1",  # Right legs
    "knee_motor_l0", "knee_motor_l1",  # Left knees
    "knee_motor_r0", "knee_motor_r1"   # Right knees
]

# Define the positions for each state (trot gait)
pos = [
    # State 0: Diagonal pairs move opposite (1,4 up, 2,3 down)
    [FRONT, BACK, -BACK, -FRONT, HI, LO, LO, HI],
    # State 1: All legs down, preparing for switch
    [FRONT, BACK, -BACK, -FRONT, HI, HI, HI, HI],
    # State 2: Opposite diagonal pairs (2,3 up, 1,4 down)
    [BACK, FRONT, -FRONT, -BACK, LO, HI, HI, LO],
    # State 3: All legs down, preparing for switch
    [BACK, FRONT, -FRONT, -BACK, HI, HI, HI, HI]
]

# Create the Robot instance
robot = Robot()

# Initialize motors
motors = []
for motor_name in motor_names:
    motor = robot.getDevice(motor_name)
    if motor:
        motors.append(motor)
        motor.setPosition(0.0)
    else:
        print(f"Could not find motor: {motor_name}")

# Main loop
elapsed = 0
while robot.step(time_step) != -1:
    elapsed += 1
    state = (elapsed // 25) % num_states
    for i in range(num_motors):
        motors[i].setPosition(pos[state][i])