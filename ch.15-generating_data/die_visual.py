from die import Die
import plotly.express as px


d6 = Die()
d10 = Die(10)

results = []
frequencies = []

for _ in range(50000):
    roll = d6.roll() + d10.roll()
    results.append(roll)

possabilities = range(2, d6.num_sides + d10.num_sides + 1)
for p in possabilities:
    frequency = results.count(p)
    frequencies.append(frequency)
    print(f"{p} : {frequency}")

title, labels = ("Rolling a d6 + d10 1000 times", {"x" : "possabilities", "y" : "Frequencies"})
fig = px.bar(x=possabilities, y=frequencies, title=title, labels=labels)

fig.update_layout(xaxis_dtick=1)
fig.write_html("d6+d10.html")
