import pandas as pd


def prepare_orders(orders: pd.DataFrame) -> pd.DataFrame:
    prepared = orders.copy()
    for column in ["product_category", "region"]:
        prepared[column] = prepared[column].astype(str).str.strip().str.title()

    prepared["order_value"] = prepared["quantity"] * prepared["unit_price"]
    prepared["order_date"] = pd.to_datetime(prepared["order_date"])
    return prepared