class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # ^
        # |

        # default

        # 0,0 N

        # GL

        # 0,1 N
        # 0,1 W

        # GL

        # -1,1 W
        # -1,1 S

        # GL

        # -1,0 S
        # -1,0 E

        # GL

        # 0,0 E
        # 0,0 N

        # => true

        coord = [0,0,'N']

        def move_robot(coord):
            if coord[2] == 'N':
                coord[1] += 1
            elif coord[2] == 'E':
                coord[0] += 1
            elif coord[2] == 'W':
                coord[0] -= 1
            else:
                coord[1] -= 1
            
        def turn_robot(coord, turn_direction):
            if turn_direction == 'L':
                if coord[2] == 'N':
                    coord[2] = 'W'
                elif coord[2] == 'E':
                    coord[2] = 'N'
                elif coord[2] == 'W':
                    coord[2] = 'S'
                else:
                    coord[2] = 'E'
            elif turn_direction == 'R':
                if coord[2] == 'N':
                    coord[2] = 'E'
                elif coord[2] == 'E':
                    coord[2] = 'S'
                elif coord[2] == 'W':
                    coord[2] = 'N'
                else:
                    coord[2] = 'W'

        # simulate one instruction set
        for i in instructions:
            if i == 'G':
                move_robot(coord)
            elif i == 'L':
                turn_robot(coord, 'L')
            else:
                turn_robot(coord, 'R')

        if (coord[0] == 0 and coord[1] == 0) or coord[2] != 'N':
            return True
        return False



