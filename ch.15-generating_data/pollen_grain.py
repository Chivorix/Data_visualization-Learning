import matplotlib.pyplot as plt
from random_walk import RandomWalk

plt.style.use("classic")
rw = RandomWalk(num_points=1000)
rw.fill_walk()
fig, ax = plt.subplots(figsize=(6,6), dpi=128)
ax.plot(rw.x_values, rw.y_values, linewidth=3)

plt.show()

