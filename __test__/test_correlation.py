import numpy as np
import matplotlib.pyplot as plt


def ex1():
    heights = [100, 120, 130, 140, 150, 160, 170, 180, 190]
    footsizes = [200, 205, 210, 220, 230, 250, 270, 280, 285]

    fig, subplots = plt.subplots(1, 1)
    subplots.scatter(heights, footsizes)

    plt.xlabel('키(cm)')
    plt.ylabel('발크기(mm)')

    plt.show()


def ex2():
    heights = [100, 200, 330, 440, 550, 560, 670, 780, 990]
    temps = [18.5, 17.5, 21, 16.2, 15, 14, 13.7, 11.2, 10]

    fig, subplots = plt.subplots(1, 1)
    subplots.scatter(heights, temps)

    plt.xlabel('산의 높이(m)')
    plt.ylabel('온도(℃)')

    plt.show()


def ex3():
    fig, subplots = plt.subplots(1, 1)
    subplots.scatter(
        np.random.random_integers(0, 100, 50),
        np.random.random_integers(0, 100, 50))

    plt.show()


if __name__ == '__main__':
    #ex1()
    #ex2()
    ex3()
