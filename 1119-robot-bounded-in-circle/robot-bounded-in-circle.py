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

        # simulate one instruction set
        for i in instructions:
            if i == 'G':
                if coord[2] == 'N':
                    coord[1] += 1
                elif coord[2] == 'E':
                    coord[0] += 1
                elif coord[2] == 'W':
                    coord[0] -= 1
                else:
                    coord[1] -= 1
            elif i == 'L':
                if coord[2] == 'N':
                    coord[2] = 'W'
                elif coord[2] == 'E':
                    coord[2] = 'N'
                elif coord[2] == 'W':
                    coord[2] = 'S'
                else:
                    coord[2] = 'E'
            else:
                if coord[2] == 'N':
                    coord[2] = 'E'
                elif coord[2] == 'E':
                    coord[2] = 'S'
                elif coord[2] == 'W':
                    coord[2] = 'N'
                else:
                    coord[2] = 'W'

        if (coord[0] == 0 and coord[1] == 0) or coord[2] != 'N':
            return True
        return False



