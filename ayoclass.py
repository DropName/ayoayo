class Ayogame:
    def __init__(self):
        self.state = [4,4,4,4,4,4,
                      4,4,4,4,4,4]
    def move(self, player, hole):
        # number of hole starting with 1 to 6
        # number of player from 1 to 2
    
        hole = hole + 6*(player - 1)
    
        if hole > 12 or hole < 1 or player < 1 or player > 2:
            return False
    
        stones = self.state[hole-1]
        self.state[hole-1] = 0
        shift = 0
    
        for i in range(stones):
            if (hole + shift + i) % 12 == (hole-1) % 12:
                shift += 1
        
            self.state[(hole + i + shift) % 12] += 1

        last_hole = (hole + stones -1 + shift) % 12
        return last_hole
    
    def round(self, player, hole):
        # move till the capture
        last_hole = self.move(player, hole) + 1
        while self.state[last_hole-1]  > 1:
            last_hole = self.move(player, last_hole) + 1

        return last_hole - 1







