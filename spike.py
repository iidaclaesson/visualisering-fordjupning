import sys

import pandas as pd
import plotly
from prepare import prepare_orders

from charts import sales_by_category

print("Python:", sys.version.split()[0])
print("Pandas:", pd.__version__)
print("Plotly:", plotly.__version__)

orders = pd.read_csv("data/orders.csv")
fig = sales_by_category(orders)

orders = prepare_orders(pd.read_csv("data/orders.csv"))

fig.write_html("chart.html")
fig.write_image("chart.png")

print("Antal traces i figuren:", len(fig.data))
print("Kategorier:", list(fig.data[0].x))
print("Värden:", list(fig.data[0].y))