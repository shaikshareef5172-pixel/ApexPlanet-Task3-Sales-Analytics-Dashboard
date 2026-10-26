from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "processed" / "cleaned_sales.csv"
PLOT_DIR = ROOT / "outputs" / "plots"
REPORT_DIR = ROOT / "reports"

PLOT_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_FILE, parse_dates=["Order_Date"])

# Core KPIs
total_revenue = df["Total_Sales"].sum()
total_orders = df["Order_ID"].nunique()
average_order_value = total_revenue / total_orders if total_orders else 0
units_sold = df["Quantity"].sum()
unique_customers = df["Customer_ID"].nunique()

kpis = {
    "Total Revenue": round(total_revenue, 2),
    "Unique Orders": int(total_orders),
    "Average Order Value": round(average_order_value, 2),
    "Units Sold": int(units_sold),
    "Unique Customers": int(unique_customers),
}

# Business breakdowns
category_sales = df.groupby("Category")["Total_Sales"].sum().sort_values(
    ascending=False
)
product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values(
    ascending=False
)
city_sales = df.groupby("City")["Total_Sales"].sum().sort_values(
    ascending=False
)

monthly_sales = (
    df.assign(Month=df["Order_Date"].dt.to_period("M").astype(str))
      .groupby("Month")["Total_Sales"]
      .sum()
      .sort_index()
)

# Chart 1: Revenue by category
plt.figure(figsize=(9, 5))
category_sales.plot(kind="bar")
plt.title("Total Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(PLOT_DIR / "revenue_by_category.png", dpi=150)
plt.close()

# Chart 2: Revenue by product
plt.figure(figsize=(9, 5))
product_sales.sort_values().plot(kind="barh")
plt.title("Total Revenue by Product")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(PLOT_DIR / "revenue_by_product.png", dpi=150)
plt.close()

# Chart 3: Monthly revenue trend
plt.figure(figsize=(11, 5))
monthly_sales.plot(marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(PLOT_DIR / "monthly_revenue.png", dpi=150)
plt.close()

# Chart 4: Revenue by city
plt.figure(figsize=(9, 5))
city_sales.sort_values().plot(kind="barh")
plt.title("Total Revenue by City")
plt.xlabel("Revenue")
plt.ylabel("City")
plt.tight_layout()
plt.savefig(PLOT_DIR / "revenue_by_city.png", dpi=150)
plt.close()

# Chart 5: Category and city comparison
pivot = pd.pivot_table(
    df,
    values="Total_Sales",
    index="City",
    columns="Category",
    aggfunc="sum",
    fill_value=0
)

plt.figure(figsize=(11, 6))
sns.heatmap(pivot, cmap="Blues", fmt=".0f")
plt.title("Revenue Heatmap: City vs Category")
plt.tight_layout()
plt.savefig(PLOT_DIR / "city_category_heatmap.png", dpi=150)
plt.close()

# Write report
report_lines = ["TASK 3 - DEEP-DIVE ANALYSIS REPORT", "", "CORE KPIs"]
for name, value in kpis.items():
    report_lines.append(f"{name}: {value:,.2f}")

report_lines.extend([
    "",
    "TOP CATEGORY BY REVENUE",
    f"{category_sales.index[0]}: {category_sales.iloc[0]:,.2f}",
    "",
    "TOP PRODUCT BY REVENUE",
    f"{product_sales.index[0]}: {product_sales.iloc[0]:,.2f}",
    "",
    "TOP CITY BY REVENUE",
    f"{city_sales.index[0]}: {city_sales.iloc[0]:,.2f}",
    "",
    "Monthly revenue is saved in outputs/plots/monthly_revenue.png.",
    "Review the monthly trend for unusual dates and business patterns.",
])

(REPORT_DIR / "deep_dive_report.txt").write_text(
    "\n".join(report_lines), encoding="utf-8"
)

print("CORE KPIs")
for name, value in kpis.items():
    print(f"{name}: {value:,.2f}")

print("\nTop category:", category_sales.index[0])
print("Top product:", product_sales.index[0])
print("Top city:", city_sales.index[0])
print("\nAnalysis complete. Check outputs/plots and reports.")