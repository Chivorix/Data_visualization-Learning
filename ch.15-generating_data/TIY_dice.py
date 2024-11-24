from die import Die
import plotly.express as px


d8 = Die(8)

x_values = []
for _ in range(1000):
    the_roll = d8.roll() + d8.roll()
    x_values.append(the_roll)

y_values = []
possabilities = range(2, d8.num_sides + d8.num_sides + 1) 
for p in possabilities:
    y_values.append(x_values.count(p))

fig = px.bar(x=possabilities, y=y_values, labels={"x" : "possabilities", "y" : "frequency"}, title="rolling two d8's a 1000 times")
fig.update_layout(xaxis_dtick=1)
fig.write_html("d8_times_two.html")
    