import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(num_points=50_000)
    rw.fill_walk()

    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15, 15), dpi=128)
    ax.scatter(rw.x_values, rw.y_values, c=rw.x_values, cmap=plt.cm.Blues, edgecolors='none',s=1)
    ax.set_aspect("equal")

    ax.scatter(0, 0, c="green", s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", s=50)
        # We emphasize the starting and ending point.

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
        # Removes the x & y ticks, making for a cneaner graph.

    plt.show()
    keep_running = input("Another walk? y/n: \n")
    if keep_running == "n":
        break