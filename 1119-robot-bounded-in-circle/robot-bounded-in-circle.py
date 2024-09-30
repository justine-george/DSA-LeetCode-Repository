class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        # 0: N
        # 1: E
        # 2: S
        # 3: W
        direction = 0
        # corresponding to N E S W
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # simulate one instruction set
        for i in instructions:
            match i:
                case 'G':
                    x += directions[direction][0]
                    y += directions[direction][1]
                case 'L':
                    direction = (direction - 1) % 4
                case 'R':
                    direction = (direction + 1) % 4

        return (x == 0 and y == 0) or direction != 0
