import pandas as pd
import pytest
from charts import sales_by_category
from prepare import prepare_orders

def test_figure_containing_categories():
    orders = prepare_orders(pd.read_csv("data/orders.csv"))
    fig = sales_by_category(orders)
    assert len(fig.data) == 1
    assert "Electronics" in fig.data[0].x

def test_hovertemplate():
    orders = prepare_orders(pd.read_csv("data/orders.csv"))
    fig = sales_by_category(orders)
    assert "%{x}" in fig.data[0].hovertemplate

def test_missing_columns():
    orders = pd.DataFrame({"product_category": ["Books"]})
    with pytest.raises(ValueError):
        sales_by_category(orders)

def test_empty_dataframe_raises():
    orders = pd.DataFrame(columns=["product_category", "order_value"])
    with pytest.raises(ValueError, match="Orders is empty"):
        sales_by_category(orders)