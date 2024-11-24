import matplotlib.pyplot as plt
from die import Die

d10 = Die(10)
x = [d10.roll() for _ in range(100)]
possabilities = range(1, d10.num_sides + 1)
y = [x.count(i) for i in possabilities]

fig, ax = plt.subplots()
ax.bar(possabilities, y, label=possabilities, width=1)
plt.show()