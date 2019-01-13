import os
from multiprocessing import Pool
from random import choice

import numpy as np
from Game import Game
from RandomPlayer import RandomPlayer


def play_random_game(_):
    players = [RandomPlayer("North"), RandomPlayer("East"), RandomPlayer("South"), RandomPlayer("West")]
    game = Game(players)
    return game.play_game(choice(players)).total_points


if __name__ == '__main__':
    pool = Pool(os.cpu_count())
    point_list = pool.map(play_random_game, range(0, 100_000))

    # point_list = list(map(play_random_game, range(0, 10_000)))

    print(np.mean(point_list))
