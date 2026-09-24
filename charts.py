import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def _validate_orders(orders: pd.DataFrame, required: set[str]) -> None:
    missing = required.difference(orders.columns)
    if missing:
        raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")

    if orders.empty:
        raise ValueError("Orders is empty, at least one row is required")


def sales_by_category(orders: pd.DataFrame) -> go.Figure:
    _validate_orders(orders, {"product_category", "order_value"})

    summary = orders.groupby("product_category", as_index=False)["order_value"].sum()
    fig = px.bar(summary, x="product_category", y="order_value")
    fig.update_traces(hovertemplate="%{x}<br>%{y:,.0f}<extra></extra>")
    fig.update_layout(separators=", ")
    return fig


def sales_over_time(orders: pd.DataFrame) -> go.Figure:
    _validate_orders(orders, {"order_date", "order_value"})
    
    summary = orders.groupby("order_date", as_index=False)["order_value"].sum()
    fig = px.line(summary, x="order_date", y="order_value")
    fig.update_traces(hovertemplate="%{x|%Y-%m-%d}<br>%{y:,.0f}<extra></extra>")
    fig.update_layout(hovermode="x unified")
    return fig


def price_vs_quantity(orders: pd.DataFrame) -> go.Figure:
    _validate_orders(orders, {"unit_price", "quantity", "product_category"})

    fig = px.scatter(orders, x="unit_price", y="quantity", color="product_category")
    fig.update_traces(hovertemplate="Price: %{x}<br>Quantity: %{y}")
    return fig