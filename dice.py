import random
from numpy import short
import plotly.figure_factory as pff

count = []
diceReserve = []

for i in range(0,100):
    dice = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceReserve.append(dice+dice2)
    count.append(i)

fig = pff.create_distplot(
    [diceReserve],['reserved']
)
fig.show()