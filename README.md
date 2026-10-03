# Sales Performance Dashboard

**Syntecxhub Virtual Internship Program — Data Analysis Track, Task 1**

> Intern: Maheen Irfan
> Domain: Data Analysis
> Program: Syntecxhub Virtual Internship

---

## Overview

This project analyzes a three-year retail sales dataset (2023–2025) to uncover revenue trends, top and bottom performing products, and regional/category sales performance. The findings are presented through an interactive web-based dashboard.

## Objective

As per the task brief, this project covers:
- Importing and cleaning a raw sales dataset (removing nulls and duplicates)
- Analyzing monthly, quarterly, and yearly sales trends
- Identifying top-selling and low-performing products
- Comparing sales across regions and product categories
- Calculating key KPIs — total revenue, profit, and growth rate
- Building an interactive dashboard to visualize all findings

## Key Results

| Metric | Value |
|---|---|
| Total Revenue | $1,043,593 |
| Total Profit | $219,778 |
| Growth Rate (2023 → 2025) | 3.36% |
| Orders Analyzed | 1,164 (after cleaning) |

**Top performing product:** Headphones ($135,985 in sales)
**Leading region:** West ($245,272 in sales)
**Leading category:** Electronics ($583,374 in sales)

## Project Structure

```
Syntecxhub_SalesPerformanceDashboard/
│
├── generate_data.py      # Generates the raw sales dataset
├── analyze.py             # Cleans data and computes KPIs/trends
├── sales_raw.csv           # Raw dataset before cleaning (1,224 rows)
├── sales_cleaned.csv       # Cleaned dataset used for analysis (1,164 rows)
├── summary.json             # Aggregated metrics consumed by the dashboard
├── dashboard.html            # Interactive dashboard (open in browser)
└── README.md
```

## Data Cleaning Summary

| Step | Detail |
|---|---|
| Raw rows | 1,224 |
| Duplicate rows removed | 24 |
| Rows with missing Sales / Profit / Region | 37 |
| **Final clean rows used for analysis** | **1,164** |

## Methodology

1. **Data generation/import** — transaction-level sales data with Order ID, date, region, category, product, quantity, sales, and profit.
2. **Cleaning** — duplicates dropped, rows with missing critical fields removed, dates parsed and broken into Year / Quarter / Month.
3. **Aggregation** — sales grouped by time period, product, region, and category to compute trends and comparisons.
4. **KPI calculation** — total revenue, total profit, and year-over-year growth rate derived from the cleaned data.
5. **Visualization** — results rendered in `dashboard.html` using Chart.js, with a dropdown to switch the sales trend chart between monthly, quarterly, and yearly views.

## How to Run

1. Make sure `dashboard.html` and `summary.json` are in the same folder.
2. Start a local server from that folder:
   ```
   python -m http.server 8000
   ```
3. Open in a browser:
   ```
   http://localhost:8000/dashboard.html
   ```

To regenerate the data and analysis from scratch:
```
python generate_data.py
python analyze.py
```

## Tools Used

- **Python (pandas)** — data cleaning, aggregation, and KPI calculation
- **Chart.js** — interactive charts (line, bar, doughnut, stacked bar)
- **HTML/CSS** — dashboard layout and styling

## Note on Tooling

Power BI/Tableau were not available in the working environment, so the dashboard was built as a standalone interactive HTML page instead. It covers the same requirements — trend analysis, KPIs, product and regional comparisons, and interactivity — and runs in any browser with no installation needed.

---

*Submitted as part of Task 1 for the Syntecxhub Data Analysis Internship.*