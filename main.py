import enum

class Command(enum.Enum):
        move = 0,
        turnLeft = 1,
        turnRight = 2,
        clear = 3

class Direction(enum.Enum):
    up = 0,
    right = 1
    down = 2,
    left = 3

def clean(room, initial, commands):
    # initial direction and location
    head = Direction.up
    location = initial

    # Process commands
    for cmd in commands:
         match cmd:
            
            # Move commands needs to know current Direction
            # Depending on the direction and next cell value move either moves to next cell
            # or else stays put
            case Command.move:
                match head:
                    case Direction.up:
                        if 0 < location[0] - 1 < len(room) and room[location[0] - 1][location[1]] == 1: 
                            location[0] = location[0] - 1
                        #else:
                        #    False
                    case Direction.down:
                        if 0 < location[0] + 1 < len(room) and room[location[0] + 1][location[1]] == 1: 
                            location[0] = location[0] + 1
                        #else:
                        #    False
                    case Direction.right:
                        if 0 < location[1] + 1 < len(room) and room[location[0]][location[1] + 1] == 1: 
                            location[1] = location[1] + 1
                        #else:
                        #    False
                    case Direction.left:
                        if 0 < location[1] - 1 < len(room) and room[location[0]][location[1] - 1] == 1: 
                            location[1] = location[1] - 1
                        #else:
                        #    False
            case Command.turnRight:
                match head:
                    case Direction.up:
                        head = Direction.right
                    case Direction.down:
                        head = Direction.left
                    case Direction.right:
                        head = Direction.down
                    case Direction.left:
                        head = Direction.up
            case Command.turnLeft:
                match head:
                    case Direction.up:
                        head = Direction.left
                    case Direction.down:
                        head = Direction.right
                    case Direction.right:
                        head = Direction.up
                    case Direction.left:
                        head = Direction.down
    
    # print last location after all commans are over
    print(location)

if __name__ == "__main__":
    # Reperents cells
    room = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [1, 0, 0, 1, 1],
        [1, 0, 0, 1, 0]
    ]
    # Any given list of commands
    commands = [Command.move, Command.move, Command.move, Command.turnRight, Command.turnLeft, Command.turnLeft, Command.move, Command.move]
    
    # Start cleaning Robot at cell (3, 3)
    clean(room, [3,3], commands)