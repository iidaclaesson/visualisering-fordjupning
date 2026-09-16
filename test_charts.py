import pandas as pd
from charts import sales_by_category

def test_figure_containing_categories():
    orders = pd.read_csv("data/orders.csv")
    fig = sales_by_category(orders)
    assert len(fig.data) == 1
    assert "Electronics" in fig.data[0].x