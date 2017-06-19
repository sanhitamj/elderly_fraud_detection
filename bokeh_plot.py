import pandas as pd
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.io import curdoc
from bokeh.models.widgets import Slider
from bokeh.layouts import column, layout


def update_slider(attrname, old, new):
   threshold=slider_threshold.value
   colors = [ 'rgba' + str((204, 102, 0, 0.2)) if r < threshold else 'rgba' + str((0, 0, 255, 0.2)) for r in df['Rank']]
   
   color_source.data = dict(fill_color=colors)


df = pd.read_csv('rank.csv', index_col=0)
x = df['AverageExpense'] 
y = df['CountPerDay'] 
rank = df['Rank']

init_threshold = 0.5
slider_threshold = Slider(start=0, end=1, step=0.001, value=init_threshold, title="Rank")

slider_threshold.on_change('value', update_slider)


#color_source = ColumnDataSource(data=dict(fill_color=['rgba' + str((0, 102, 0, 0.3))] ))

color_source = ColumnDataSource(data=dict(fill_color=['rgba' + str((204, 102, 0, 0.2)) if r < init_threshold else 'rgba' + str((0, 0, 255, 0.2)) for r in df['Rank']]))



p = figure(title="Marking outliers", x_axis_label='Total Expense', 
           y_axis_label='Total Number of Transactions')


radii = df['Rank'] * x.median() + 7500



p.circle(x, y, radius=radii, fill_color='fill_color', source=color_source, line_color=None)

r = column(p,  slider_threshold )
curdoc().add_root(r)


