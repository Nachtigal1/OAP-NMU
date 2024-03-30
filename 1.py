import math
import matplotlib.pyplot as plt
import numpy as np

def y1(x: float) -> float:
    return 5 * math.sin(1 / x) * math.cos(x ** 2 + 1 / x) ** 2

def y2(x: float) -> float:
    return 5 * math.sin(1 / x) * math.cos(x ** 2) ** 3

def y1_arr(x_arr: list[float]) -> list[float]:
    new_x_arr = []
    for i in range(len(x_arr)):
        new_x_arr.append(y1(x_arr[i]))
    return new_x_arr

def y2_arr(x_arr: list[float]) -> list[float]:
    new_x_arr = []
    for i in range(len(x_arr)):
        new_x_arr.append(y2(x_arr[i]))
    return new_x_arr

def prepare_x1_and_x2() -> tuple[list[float], list[float]]:
    x1, x2 = [], []
    for i in np.arange(1, 4, 0.01):
        x1.append(i)
    for i in np.arange(-4, 4, 0.01):
        x2.append(i)
    return x1, x2

def one_plot_solution(x1, x2: list[float]):
    plt.plot(x1, y1_arr(x1))
    plt.plot(x2, y2_arr(x2))
    plt.show()

def subplots_solution(x1, x2: list[float]):
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].plot(x1, y1_arr(x1))
    axs[1].plot(x2, y2_arr(x2))
    plt.show()

def main():
    x1, x2 = prepare_x1_and_x2()
    one_plot_solution(x1, x2)
    subplots_solution(x1, x2)

if __name__ == "__main__":
    main()
