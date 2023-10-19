import copy

class Ayogame:
    def __init__(self):
        """
        state -- is a board configuration
        score -- player score
        """
        self.state = [4,4,4,4,4,4,
                      4,4,4,4,4,4]
        self.score = [0,0]


    def __str__(self):
        return str(self.state[6:][::-1]) + '\n' + str(self.state[:6])


    def step(self, hole):
        """
        does one iteration by taking all stones from 'hole' 
        and dealing stones to the next holes
        return the last hole number
        """
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
        """
        makes 'steps' until dealing the last stone to the empty hole
        returns number of the last hole
        """
    
        last_hole = self.step(hole)
        while self.state[last_hole] > 1:
            last_hole = self.step(last_hole)

        return last_hole


    def capture(self, player, hole):
        """
        captures stones, if they are on the opposite side
        adds a score to the 'player'
        """
        if hole < 6:
            self.score[player-1] += self.state[11 - hole]
            self.state[11 - hole] = 0

            return True

        else:
            return False

    
    def switch(self):
        """
        reverts board, so the second player becomes the first
        """
        self.state = self.state[6:] + self.state[:6]

        return 0

    def check_illegal(self, hole):
        if self.state[hole] == 0 or hole > 5:
            return False

        a = copy.deepcopy(self)
        last_hole = a.move(hole)
        if a.capture(1, last_hole):
            return True
        elif a.state[6:][::-1] == [0]*6:
            return False
        else:
            return True


    def round(self, player, hole):
         
        last_hole = self.move(hole)
        self.capture(player, last_hole)
        self.switch()

        return (player+1) % 2

    def game_loud(self, player):
         
        print('The score is {}'.format(self.score))
        print('Player {} turn:'.format(player+1))
        print(self)
        print('==========')


        return player


