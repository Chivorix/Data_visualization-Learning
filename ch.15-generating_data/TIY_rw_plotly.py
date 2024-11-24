import plotly.express as px
import plotly.graph_objects as go   
import matplotlib.pyplot as plt
from die import Die
from random_walk import RandomWalk

rw = RandomWalk(num_points=1000)
rw.fill_walk()

fig = go.Figure()
    # Designed for multiple layers of traces
fig.add_scatter(x=rw.x_values, y=rw.y_values, mode='lines+markers', name="Random Walk")
fig.add_scatter(x=[rw.x_values[0]], y=[rw.y_values[0]], mode='markers', name="Starting Point",  marker=dict(color='green', size=12))
fig.add_scatter(x=[rw.x_values[-1]], y=[rw.y_values[-1]], mode='markers', name="End Point",  marker=dict(color='red', size=12))



fig.write_html("rw_plotly.html")


