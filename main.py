import numpy as np
from sort import bubble_sort
import matplotlib.pyplot as plt
import load_data


if __name__ == "__main__":
    data = load_data.load_data('activity.csv')
    power_W = data['PowerOriginal']
    print(power_W)
    sorted_power_W = bubble_sort(power_W)
    print(sorted_power_W[::-1])
    plt.plot(sorted_power_W[::-1])
    plt.ylabel('Power (W)')
    plt.xlabel('Time (s)')
    plt.show()