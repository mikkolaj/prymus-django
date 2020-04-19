import csv

from math import pi

import pandas as pd

from bokeh.io import output_file, show
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum
from bokeh.layouts import row as rw


infected = {}
infmin = float('inf')
recovered = {}
recmin = float('inf')


with open('dane.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        if "Recovered" not in row[-1]:
            # infected people
            if len(infected) < 10:
                infected[row[-1]] = int(row[-5])
                if int(row[-5]) < infmin:
                    infmin = int(row[-5])
            else:
                if int(row[-3]) > infmin:
                    infected = {key: val for key, val in infected.items() if val != infmin}
                    infected[row[-1]] = int(row[-5])
                    infmin = min(infected.values())

            # recovered people
            if len(recovered) < 10:
                recovered[row[-1]] = int(row[-3])
                if int(row[-3]) < recmin:
                    recmin = int(row[-3])
            else:
                if int(row[-3]) > recmin:
                    recovered = {key: val for key, val in recovered.items() if val != recmin}
                    recovered[row[-1]] = int(row[-3])
                    recmin = min(recovered.values())

infected = {k: v for k, v in sorted(infected.items(), key=lambda item: item[1])}
recovered = {k: v for k, v in sorted(recovered.items(), key=lambda item: item[1])}

output_file("pie.html")


data = pd.Series(infected).reset_index(name='value').rename(columns={'index': 'country'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20c[len(infected)]

p = figure(plot_height=350, title="Potwierdzone przypadki COVID-19", toolbar_location=None,
           tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='country', source=data)

p.axis.axis_label = None
p.axis.visible = False
p.grid.grid_line_color = None


data2 = pd.Series(recovered).reset_index(name='value').rename(columns={'index': 'country'})
data2['angle'] = data2['value']/data2['value'].sum() * 2*pi
data2['color'] = Category20c[len(recovered)]

p2 = figure(plot_height=350, title="Osoby z wyleczonym COVID-19", toolbar_location=None,
           tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

p2.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='country', source=data2)

p2.axis.axis_label = None
p2.axis.visible = False
p2.grid.grid_line_color = None

show(rw(p, p2))


