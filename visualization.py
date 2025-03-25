import pandas as pd
from bokeh.plotting import figure, show

def visualize():
    # x = [1, 2, 3]
    # x = [pd.to_datetime("3/15"), pd.to_datetime("3/16"), pd.to_datetime("3/17")]
    x = ['3/15', '3/16', '3/17']
    y = [1800, 2500, 3400]
    
    p = figure(title="Calories per day", x_axis_label="Date", y_axis_label="Calories", x_range=x)
    p.vbar(x=x, top=y, legend_label='Calories Consumed', width=0.5, bottom=0, color='red')
    show(p)