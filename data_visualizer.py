import matplotlib.pyplot as plt
import json

plt.gca().invert_yaxis()
with open("dots.json", 'r') as file:
    dataset = json.load(file)
    plt.gca().invert_yaxis()
    for data in dataset:
        plt.plot(data[0], data[1], 'bo' if data[2] == 0 else 'ro')
plt.show()