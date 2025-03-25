import pandas as pd
from bokeh.plotting import figure, show
from math import pi
from bokeh.palettes import Category20c
from bokeh.transform import cumsum

def visualize():
    # x = [1, 2, 3]
    # x = [pd.to_datetime("3/15"), pd.to_datetime("3/16"), pd.to_datetime("3/17")]
    x = ['3/15', '3/16', '3/17']
    y = [1800, 2500, 3400]
    
    p = figure(title="Calories per day", x_axis_label="Date", y_axis_label="Calories", x_range=x)
    p.vbar(x=x, top=y, legend_label='Calories Consumed', width=0.5, bottom=0, color='red')
    # show(p)


    pie = {
        # 'Protein': 23,
        'Fiber': 11,
        'Carbs': 223,
        'Fat': 123
    }

    data = pd.Series(pie).reset_index(name='value').rename(columns={'index': 'macros'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = Category20c[len(pie)]

    d = figure(title='Pie', toolbar_location=None,
               tools='hover', tooltips='@macros: @value', x_range=(-0.5, 1.0))
    d.wedge(x=0, y=1, radius=0.4, start_angle=cumsum('angle', include_zero=True),
            end_angle=cumsum('angle'), line_color='white', fill_color='color',
            legend_field='pie', source=data)
    d.axis.axis_label = None
    d.axis.visible = False
    d.grid.grid_line_color = None

    show(d)
