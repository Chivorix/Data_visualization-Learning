import plotly.express as px
from die import Die

d6 = Die()

x_values = [(d6.roll() * 3) for _ in range(1000)]
possabilities = range(3, ((d6.num_sides * 3) + 1))
y_values = [x_values.count(p) for p in possabilities]

fig = px.bar(
    x=possabilities,
    y=y_values, 
    title="rolling 3 d6's", 
    labels={"x":"POSSABILITIES", "y":"FREQUENCY"},
    color_discrete_sequence=["red"]
    )
fig.update_layout(
    xaxis_dtick=1,
    title={"font":{"size":24}},
    xaxis_title={"font":{"size":32}},
    yaxis_title={"font":{"size":32}}
    )
fig.write_html("d6x3.html")