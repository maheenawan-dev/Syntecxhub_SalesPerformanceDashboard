import pandas as pd
import json

df = pd.read_csv("sales_raw.csv", parse_dates=["OrderDate"])
print("Before cleaning:", len(df), "rows | Nulls:", df.isnull().sum().sum(), "| Duplicates:", df.duplicated().sum())

df_clean = df.drop_duplicates().dropna(subset=["Sales","Profit","Region"])
df_clean["Year"] = df_clean["OrderDate"].dt.year
df_clean["Quarter"] = df_clean["OrderDate"].dt.to_period("Q").astype(str)
df_clean["Month"] = df_clean["OrderDate"].dt.to_period("M").astype(str)
df_clean.to_csv("sales_cleaned.csv", index=False)
print("After cleaning:", len(df_clean), "rows")

total_revenue = df_clean["Sales"].sum()
total_profit = df_clean["Profit"].sum()
yearly = df_clean.groupby("Year")["Sales"].sum().sort_index()
growth_rate = ((yearly.iloc[-1] - yearly.iloc[0]) / yearly.iloc[0]) * 100

summary = {
    "total_revenue": round(total_revenue,2),
    "total_profit": round(total_profit,2),
    "growth_rate_pct": round(growth_rate,2),
    "total_orders": len(df_clean),
    "monthly_trend": {k: round(v,2) for k,v in df_clean.groupby("Month")["Sales"].sum().sort_index().items()},
    "quarterly_trend": {k: round(v,2) for k,v in df_clean.groupby("Quarter")["Sales"].sum().sort_index().items()},
    "yearly_trend": {str(k): round(v,2) for k,v in yearly.items()},
    "top5_products": {k: round(v,2) for k,v in df_clean.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(5).items()},
    "bottom5_products": {k: round(v,2) for k,v in df_clean.groupby("Product")["Sales"].sum().sort_values(ascending=False).tail(5).items()},
    "region_sales": {k: round(v,2) for k,v in df_clean.groupby("Region")["Sales"].sum().sort_values(ascending=False).items()},
    "category_sales": {k: round(v,2) for k,v in df_clean.groupby("Category")["Sales"].sum().sort_values(ascending=False).items()},
    "region_category": df_clean.groupby(["Region","Category"])["Sales"].sum().unstack().fillna(0).round(2).to_dict()
}

with open("summary.json","w") as f:
    json.dump(summary, f, indent=2)

print("Total Revenue:", summary["total_revenue"])
print("Total Profit:", summary["total_profit"])
print("Growth Rate %:", summary["growth_rate_pct"])