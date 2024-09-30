from enum import Enum

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        '''
        direction = 0, 1, 2, 3: N, E, S, W
        '''
        x, y = 0, 0
        direction = Direction.NORTH
        directions = {
            Direction.NORTH: (0,1),
            Direction.EAST: (1,0),
            Direction.SOUTH: (0,-1),
            Direction.WEST: (-1,0)
        }

        for i in instructions:
            match i:
                case 'G':
                    dx, dy = directions[direction]
                    x += dx
                    y += dy
                case 'L':
                    direction = Direction((direction.value - 1) % 4)
                case 'R':
                    direction = Direction((direction.value + 1) % 4)
        
        return x == y == 0 or direction != Direction.NORTH