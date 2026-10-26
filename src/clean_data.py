from pathlib import Path
import pandas as pd

# Project paths
ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = ROOT / "data" / "raw" / "ApexPlanet_DataAnalytics_Dataset.xlsx"
OUTPUT_DIR = ROOT / "data" / "processed"
REPORT_DIR = ROOT / "reports"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

# Load original data
df = pd.read_excel(RAW_FILE)

# Standardize column names and text values
df.columns = df.columns.str.strip()

text_columns = df.select_dtypes(include="object").columns
for col in text_columns:
    df[col] = df[col].apply(
        lambda x: x.strip() if isinstance(x, str) else x
    )

# Convert dates and numeric fields
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"], errors="coerce"
)

for col in ["Age", "Quantity", "Unit_Price", "Total_Sales"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Save quality findings before handling missing values
duplicate_rows = int(df.duplicated().sum())
duplicate_order_rows = int(df["Order_ID"].duplicated().sum())
missing_before = df.isna().sum()

# Apply consistent missing-value rules
df["Age"] = df["Age"].fillna(df["Age"].median())
df["City"] = df["City"].fillna("Unknown")

# Remove only fully duplicated rows
df = df.drop_duplicates()

# Recalculate revenue for validation, not automatic replacement
df["Calculated_Sales"] = df["Quantity"] * df["Unit_Price"]
sales_mismatch = int(
    (
        (df["Calculated_Sales"] - df["Total_Sales"]).abs() > 0.02
    ).sum()
)

# Remove helper column after validation
df = df.drop(columns=["Calculated_Sales"])

# Export cleaned data
output_file = OUTPUT_DIR / "cleaned_sales.csv"
df.to_csv(output_file, index=False)

# Export data quality report
report = [
    "APEXPLANET TASK 3 - DATA QUALITY REPORT",
    f"Rows after cleaning: {len(df)}",
    f"Columns: {len(df.columns)}",
    f"Fully duplicated rows before cleaning: {duplicate_rows}",
    f"Repeated Order_ID rows before cleaning: {duplicate_order_rows}",
    f"Missing Age values before cleaning: {int(missing_before['Age'])}",
    f"Missing City values before cleaning: {int(missing_before['City'])}",
    f"Revenue calculation mismatches: {sales_mismatch}",
    f"Date range: {df['Order_Date'].min()} to {df['Order_Date'].max()}",
    f"Cleaned CSV: {output_file}",
]

(REPORT_DIR / "data_quality_report.txt").write_text(
    "\n".join(report), encoding="utf-8"
)

print("\n".join(report))
print("\nData cleaning completed successfully.")