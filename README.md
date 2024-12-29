### README: Quadruped Robot Gait and Turn Controller

---

#### **Project Overview**
This project demonstrates the control of a quadruped robot in Webots simulation software. The robot is equipped with eight motors, two per leg, and operates using predefined gaits and turning maneuvers.

The project includes two controllers: 
1. **`drive_robot`**: Implements a trot gait for forward movement.
2. **`drive_robot_turn`**: Implements a turning motion for clockwise rotation.

The simulation environment is defined in the `hexapod.wbt` world file.

---

#### **Directory Structure**
```
├── controllers/
│   ├── drive_robot/
│   │   └── drive_robot.py        # Trot gait controller
│   └── drive_robot_turn/
│       └── drive_robot_turn.py   # Turning controller
└── worlds/
    └── hexapod.wbt               # Simulation world file
```

---

#### **Controller Details**

##### **1. Trot Gait Controller (`drive_robot.py`)**
This script simulates a trot gait, where diagonal leg pairs move in sync for balanced and stable movement.

- **States**:
  - **State 0**: Diagonal leg pairs alternate (front-left, back-right up; front-right, back-left down).
  - **State 1**: All legs prepare to switch positions.
  - **State 2**: Opposite diagonal pairs alternate.
  - **State 3**: Reset state for a smooth transition.

- **Position Settings**:
  - `FRONT` and `BACK` for hip motors.
  - `HI` and `LO` for knee motors.

- **Main Features**:
  - Cyclic transitions between states for continuous movement.
  - Step interval of 25 cycles for smooth motion.

##### **2. Turning Controller (`drive_robot_turn.py`)**
This script enables clockwise turning by adjusting leg positions to mimic a pivoting motion.

- **States**:
  - **Outer Radius**: Legs on the left side extend further than legs on the right.
  - **Inner Radius**: Legs on the right side retract to create the turning effect.

- **Position Settings**:
  - `TURN_OUTER` for extended angles on the outer legs.
  - `TURN_INNER` for retracted angles on the inner legs.

- **Main Features**:
  - Clockwise rotation with synchronized leg movement.
  - Smooth transitions between states for realistic turning.

---

#### **Requirements**
- **Software**: 
  - Webots (Robot simulation software)
- **Hardware**: None (simulation-only).

---

#### **Usage**
1. **Launch the Webots Simulation**:
   - Open Webots and load the `hexapod.wbt` world file from the `worlds` directory.

2. **Run the Controllers**:
   - Select the `drive_robot` controller to simulate forward trotting motion.
   - Select the `drive_robot_turn` controller to simulate clockwise turning.

3. **Simulation Parameters**:
   - Time step: 16 ms.
   - State transition: Every 25 steps.

---

#### **Customization**
- Adjust the `FRONT`, `BACK`, `TURN_OUTER`, and `TURN_INNER` constants in the scripts to modify leg motion.
- Experiment with different state transition intervals by changing the `elapsed` and `state` calculations.

---