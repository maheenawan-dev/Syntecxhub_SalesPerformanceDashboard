import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

regions = ["North", "South", "East", "West", "Central"]
categories = {
    "Electronics": ["Smartphone", "Laptop", "Headphones", "Tablet", "Smartwatch"],
    "Furniture": ["Office Chair", "Desk", "Bookshelf", "Sofa", "Dining Table"],
    "Clothing": ["T-Shirt", "Jeans", "Jacket", "Shoes", "Cap"],
    "Groceries": ["Rice Bag", "Cooking Oil", "Snacks Pack", "Beverages", "Spices"],
    "Stationery": ["Notebook", "Pen Set", "Backpack", "Printer Paper", "Desk Organizer"]
}
segments = ["Consumer", "Corporate", "Home Office"]

start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 12, 31)
date_range_days = (end_date - start_date).days

rows = []
order_id = 1000
for i in range(1200):
    order_id += 1
    order_date = start_date + timedelta(days=random.randint(0, date_range_days))
    region = random.choice(regions)
    category = random.choice(list(categories.keys()))
    product = random.choice(categories[category])
    segment = random.choice(segments)
    quantity = random.randint(1, 10)
    base_price = {
        "Electronics": random.uniform(80, 900), "Furniture": random.uniform(60, 500),
        "Clothing": random.uniform(10, 90), "Groceries": random.uniform(3, 40),
        "Stationery": random.uniform(2, 60)
    }[category]
    sales = round(base_price * quantity, 2)
    profit = round(sales * random.uniform(0.08, 0.35), 2)
    rows.append([order_id, order_date.strftime("%Y-%m-%d"), region, category, product, segment, quantity, sales, profit])

df = pd.DataFrame(rows, columns=["OrderID","OrderDate","Region","Category","Product","Segment","Quantity","Sales","Profit"])

null_idx = df.sample(frac=0.03, random_state=1).index
for idx in null_idx:
    col = random.choice(["Sales","Profit","Region"])
    df.loc[idx, col] = np.nan

dup_rows = df.sample(frac=0.02, random_state=2)
df = pd.concat([df, dup_rows], ignore_index=True)
df.to_csv("sales_raw.csv", index=False)
print("Raw rows:", len(df))