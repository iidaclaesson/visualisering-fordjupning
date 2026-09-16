import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def sales_by_category(orders: pd.DataFrame) -> go.Figure:
    summary = orders.groupby("product_category", as_index=False)["unit_price"].sum()
    return px.bar(summary, x="product_category", y="unit_price")