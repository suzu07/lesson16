import random
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
from random import choice


def montyhall(N):
    changer_win = 0
    straight_win = 0
    p_changer_win = []
    p_straight_win = []
    for i in range(N):
        doors = [0, 1, 2]
        answer = random.choice(doors)
        player_select = random.choice(doors)
        if player_select == answer:
            while True:
                open_sel = random.choice(doors)
                if open_sel != player_select:
                    break
        elif player_select != answer:
            while True:
                open_sel = random.choice(doors)
                if open_sel != answer and open_sel != player_select:
                    break
        while True:
            no_sel = random.choice(doors)
            if not no_sel == open_sel and not no_sel == player_select:
                break

        if no_sel == answer:
            changer_win += 1
        else:
            straight_win += 1
        p_changer_win.append(changer_win / (straight_win + changer_win))
        p_straight_win.append(straight_win / (straight_win + changer_win))
    return changer_win, straight_win, p_changer_win, p_straight_win


def main():
    n = 10000
    changer_win, straight_win, p_changer_win, p_straight_win = montyhall(n)
    print("changer_win=", changer_win, "p_changer_win =", p_changer_win[-1])
    print("straight_win=", straight_win, "p_straight_win=", p_straight_win[-1])
    plt.plot(p_changer_win, label='P_changed_wins')
    plt.plot(p_straight_win, label='P_unchanged_wins')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
