class Ayogame:
    def __init__(self):
        self.state = [4,4,4,4,4,4,
                      4,4,4,4,4,4]
        self.score = [0,0]

    def move(self, hole):
        # number of hole starting with 0 to 5
    
        stones = self.state[hole]
        self.state[hole] = 0
        shift = 0
    
        for i in range(stones):
            if (hole + 1 + shift + i) % 12 == (hole) % 12:
                shift += 1
        
            self.state[(hole + 1 + i + shift) % 12] += 1

        last_hole = (hole + stones  + shift) % 12
        return last_hole
    
    def round(self, player, hole):
        # move till the capture
    
        last_hole = self.move(hole)
        while self.state[last_hole] > 1:
            last_hole = self.move(last_hole)
            
        if last_hole < 6:
            self.score[player-1] = self.state[11 - last_hole]
            self.state[11 - last_hole] = 0

        return last_hole







