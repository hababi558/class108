import plotly.figure_factory as pff
import csv
import pandas as pd

data = pd.read_csv('data.csv')

fig = pff.create_distplot(
    [data['Height(Inches)'].tolist()],['height'],show_hist=False
)

fig.show()