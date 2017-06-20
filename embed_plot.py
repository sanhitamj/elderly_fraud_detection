'''
To run this bokeh program file -

bokeh serve --show plot.py

'''

import pandas as pd
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.io import curdoc
from bokeh.models.widgets import Slider
from bokeh.layouts import column, layout
from bokeh.embed import components

def update_slider(attrname, old, new):
   threshold=slider_threshold.value
   colors = [ 'rgba' + str((25, 10, 255, 0.2)) if r < threshold else 'rgba' + str((255, 26, 10, 0.8)) for r in df['Rank']]
   color_source.data['fill_color']=colors

output_file('outliers.html')
df = pd.read_csv('rank.csv', index_col=0)
threshold_init = 0.762

x = df['Total Expense']
y = df['Counts']
radii = df['Rank'] * x.median() + 5000
colors = [ 'rgba' + str((25, 10, 255, 0.2)) if r < threshold_init else 'rgba' + str((255, 26, 10, 0.8)) for r in df['Rank']]

slider_threshold = Slider(start=0, end=1, step=0.001, value=threshold_init, title="Rank")

color_source = ColumnDataSource(data=dict(x=x, y=y, rad=radii, fill_color=colors))

TOOLS="resize, pan, wheel_zoom, box_zoom, reset, box_select, lasso_select"

p = figure(tools = TOOLS, title="Marking outliers", x_axis_label='Total Expense',
           y_axis_label='Total Number of Transactions')

p.circle(x='x', y='y', radius='rad', fill_color='fill_color', source=color_source, fill_alpha=1, line_color=None)

slider_threshold.on_change('value', update_slider)

curdoc().add_root( column(p, slider_threshold) )
