from controller import Robot

# Constants
time_step = 16
num_motors = 8
num_states = 6

# Modified constants for turning
FRONT = +0.7
BACK = -0.7
TURN_OUTER = +0.7  # Larger angle for outer legs
TURN_INNER = +0.3  # Smaller angle for inner legs
HI = +0.02
LO = -0.02

motor_names = [
    "hip_motor_l0", "hip_motor_l1", 
    "hip_motor_r0", "hip_motor_r1", 
    "knee_motor_l0", "knee_motor_l1", 
    "knee_motor_r0", "knee_motor_r1"
]

# Modified positions for turning (clockwise rotation)
pos = [
    # Left side uses larger angles (outer radius), right side uses smaller angles (inner radius)
    [TURN_OUTER, FRONT, -TURN_INNER, -BACK, LO, HI, HI, LO],
    [TURN_OUTER, FRONT, -TURN_INNER, -BACK, HI, HI, HI, HI],
    [TURN_OUTER, FRONT, -TURN_INNER, -BACK, HI, LO, LO, HI],
    [FRONT, TURN_OUTER, -BACK, -TURN_INNER, HI, LO, LO, HI],
    [FRONT, TURN_OUTER, -BACK, -TURN_INNER, HI, HI, HI, HI],
    [FRONT, TURN_OUTER, -BACK, -TURN_INNER, LO, HI, HI, LO]
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
    state = (elapsed // 25 + 1) % num_states
    for i in range(num_motors):
        motors[i].setPosition(pos[state][i])
