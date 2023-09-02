class Ayogame:
    def __init__(self):
        self.state = [4,4,4,4,4,4,
                      4,4,4,4,4,4]
        self.score = [0,0]

    def step(self, hole):
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
    
    def move(self, hole):
        # move till the capture
    
        last_hole = self.step(hole)
        while self.state[last_hole] > 1:
            last_hole = self.step(last_hole)

        return last_hole

    def capture(self, player, hole):
        if hole < 6:
            self.score[player-1] = self.state[11 - hole]
            self.state[11 - hole] = 0

            return True

        else:
            return False

    
    def switch(self):
        self.state = self.state[6:] + self.state[:6]

        return 0





