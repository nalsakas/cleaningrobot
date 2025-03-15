# cleaningrobot
Find last position of cleaning Robot after series of command in a given grid of cells

## Problem Statement:
For a given m x n grid (cells), 0s represents walls and 1s represents empty cells.
Robot can't pass through walls (0s), only allowed to move among empty cells (1s).
Robot will be given a series of commands, find final postion of the robot.
After each Move command, robot tries to move forward cell if it is empty or
returns False otherwise. TurnLeft and TurnRight commands rotates the front of the robot.
Lastly Clean command cleans the cell but doesn't moves or rotates the front of robot.  

## Solution:
- Define Direction enum
- Define Command enum
- Inititalize starting Direction and cell position
- Apply all commands
- Get last cell position