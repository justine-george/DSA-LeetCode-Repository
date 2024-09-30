class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        '''
        direction = 0, 1, 2, 3: N, E, S, W
        '''
        
        x, y, direction = 0, 0, 0
        directions = [
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        ]

        for i in instructions:
            match i:
                case 'G':
                    x += directions[direction][0]
                    y += directions[direction][1]

                case 'L':
                    direction = (direction - 1) % 4

                case 'R':
                    direction = (direction + 1) % 4

        
        return x == y == 0 or direction != 0