import sys

import pandas as pd
import plotly
from prepare import prepare_orders

from charts import sales_by_category, sales_over_time, price_vs_quantity

print("Python:", sys.version.split()[0])
print("Pandas:", pd.__version__)
print("Plotly:", plotly.__version__)

orders = prepare_orders(pd.read_csv("data/orders.csv"))

category_fig = sales_by_category(orders)
category_fig.write_html("category_chart.html")
category_fig.write_image("category_chart.png")

time_fig = sales_over_time(orders)
time_fig.write_html("time_chart.html")
time_fig.write_image("time_chart.png")

scatter_fig = price_vs_quantity(orders)
scatter_fig.write_html("scatter_chart.html")
scatter_fig.write_image("scatter_chart.png")

print("Categories:", category_fig.data[0].x.tolist())
print("Sales:", category_fig.data[0].y.tolist())
print("Days with sales:", len(time_fig.data[0].x))