from pathlib import Path
import sys

import pandas as pd
import plotly

from prepare import prepare_orders
from charts import sales_by_category, sales_over_time, price_vs_quantity

print("Python:", sys.version.split()[0])
print("Pandas:", pd.__version__)
print("Plotly:", plotly.__version__)

orders = prepare_orders(pd.read_csv("data/orders.csv"))

Path("output").mkdir(exist_ok=True)

category_fig = sales_by_category(orders)
category_fig.write_html("output/category_chart.html")
category_fig.write_image("output/category_chart.png")

time_fig = sales_over_time(orders)
time_fig.write_html("output/time_chart.html")
time_fig.write_image("output/time_chart.png")

scatter_fig = price_vs_quantity(orders)
scatter_fig.write_html("output/scatter_chart.html")
scatter_fig.write_image("output/scatter_chart.png")

print("Categories:", category_fig.data[0].x.tolist())
print("Sales:", category_fig.data[0].y.tolist())
print("Days with sales:", len(time_fig.data[0].x))