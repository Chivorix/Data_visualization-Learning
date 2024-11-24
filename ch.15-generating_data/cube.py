import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.set_size_inches(14,6)
ax.set_title("Cubing_Numbers")
ax.set_xlabel("Values")
ax.set_ylabel("Cubed_values")

x = [i for i in range(1,5001)]
y = [(i**3) for i in x]

ax.scatter(x, y, c=y, cmap=plt.cm.Blues , s=5)
ax.ticklabel_format(style="plain")

plt.savefig("Cube_assignment", bbox_inches="tight")

