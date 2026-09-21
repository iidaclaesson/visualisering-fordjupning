import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def sales_by_category(orders: pd.DataFrame) -> go.Figure:
    required = {"product_category", "order_value"}
    missing = required.difference(orders.columns)
    if missing:
        raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")

    if orders.empty:
        raise ValueError("Orders is empty, at least one row is required")

    summary = orders.groupby("product_category", as_index=False)["order_value"].sum()
    fig = px.bar(summary, x="product_category", y="order_value")
    fig.update_traces(hovertemplate="%{x}<br>%{y:,.0f}<extra></extra>")
    return fig


def sales_over_time(orders: pd.DataFrame) -> go.Figure:
    required = {"order_date", "order_value"}
    missing = required.difference(orders.columns)
    if missing:
        raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")
    if orders.empty:
        raise ValueError("Orders is empty, at least one row is required")

    
    summary = orders.groupby("order_date", as_index=False)["order_value"].sum()
    fig = px.line(summary, x="order_date", y="order_value")
    fig.update_traces(hovertemplate="%{x|%Y-%m-%d}<br>%{y:,.0f}<extra></extra>")
    fig.update_layout(hovermode="x unified")
    return fig