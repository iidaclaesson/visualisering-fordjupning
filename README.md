# Interactive visualisations with Plotly

## Overview

A project exploring how interactivity works in Plotly and how it is controlled.

`charts.py` has functions that return finished, interactive figures from order data: a bar chart, a time series and a scatter plot. Each figure demonstrates a different sort of interaction: hovering, zooming and selecting.

The tests check the structure of the figures and not how they look. 

## Setup
Requires Python 3.11 or later.

Create and activate a virtual environment and then:
```
pip install -r requirements.txt
```
- This installs pandas, plotly, pytest and kaleido

## Usage

```
python main.py
```
- Creates six files in `output/`: three interactive HTML charts and three static PNG images 

Run tests:
```
python -m pytest
```

## Data

`data/orders.csv` contains 80 orders from January 2026 to March 2026, which is reused from a separate course assignment.

Columns: order id, date, customer, region, product category, quantity, unit price, discount and returned.

`prepare.py` adds an `order_value` column (quantity * unit price).

No external services are required. 
