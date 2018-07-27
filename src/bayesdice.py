import numpy as np
import pandas as pd
import random


class BayesDice:
    def __init__(self, _id, sides, expected_avg, roll):
        self._id = _id
        self.sides = sides
        self.expected_avg = expected_avg

    def sides(self):
        random.choice([4,6,8,12 20])

    def expected_avg(self):
        nums = []
        for num in range(1,self.sides+1):
            nums.append(num)
        self.sides.mean()

    def roll(self):
        return random.randrange(1, self.sides + 1)

    def __str__(self):
        return "Die ID: {} with {} sides".format(self._id, self._sides)

    def __repr__(self):
        return self.__str__()


# bd = BayesDice()
# bd.choose_die()
# bd.roll_die()
# bd.roll_die()
# bd.roll_die()
