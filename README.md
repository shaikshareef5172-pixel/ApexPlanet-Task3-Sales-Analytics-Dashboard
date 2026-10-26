
ApexPlanet Task 3: Sales Analytics Dashboard

Project Overview

This project was developed as part of my Data Analytics Internship at ApexPlanet Software Pvt. Ltd.

The objective of this project is to analyze sales data, identify important business insights, understand revenue trends, and build an interactive dashboard using Microsoft Power BI.

The project combines Python-based data cleaning and exploratory data analysis with Power BI visualizations to present sales performance clearly.

Project Objectives

- Clean and prepare sales data for analysis.
- Identify and handle missing values and data quality issues.
- Perform exploratory data analysis (EDA).
- Analyze revenue by product, category, and city.
- Examine monthly revenue trends.
- Calculate important sales KPIs.
- Build an interactive Power BI dashboard for business insights.

Tools and Technologies

- Python — Data analysis and processing
- Pandas — Data cleaning and manipulation
- Matplotlib / Seaborn — Data visualization
- Microsoft Power BI Desktop — Interactive dashboard development
- Visual Studio Code — Development environment
- Excel and CSV — Data storage and processing

Dataset Description

The project uses the ApexPlanet sales analytics dataset.

The dataset contains information related to:

- Order date and order identification
- Customer information
- City
- Product category
- Product
- Quantity sold
- Unit price
- Total sales

The original Excel dataset is stored separately from the processed data to preserve the source file.

Project Structure

ApexPlanet-Task3-Sales-Analytics-Dashboard/
│
├── data/
│   ├── raw/
│   │   └── ApexPlanet_DataAnalytics_Dataset.xlsx
│   │
│   └── processed/
│       └── cleaned_sales.csv
│
├── outputs/
│   └── plots/
│       ├── city_category_heatmap.png
│       ├── monthly_revenue.png
│       ├── revenue_by_category.png
│       ├── revenue_by_city.png
│       └── revenue_by_product.png
│
├── reports/
│   ├── data_quality_report.txt
│   └── deep_dive_report.txt
│
├── src/
│   ├── clean_data.py
│   └── deep_dive_analysis.py
│
├── requirements.txt
├── ApexPlanet_Task3_Dashboard.pbix
└── README.md

Data Cleaning and Preparation

Python and Pandas were used to prepare the dataset for analysis.

The main activities included:

- Inspecting the dataset structure and data types.
- Checking missing values and duplicate records.
- Standardizing text fields.
- Converting order dates into an appropriate date format.
- Handling missing values.
- Saving the cleaned dataset as a separate CSV file.
- Generating a data quality report.

Exploratory Data Analysis

Exploratory data analysis was performed to understand sales performance and identify useful business patterns.

The analysis includes:

- Monthly revenue trends.
- Revenue by product category.
- Revenue by city.
- Revenue by product.
- City and category comparisons.
- Summary statistics and key performance indicators.

The generated charts are available in the "outputs/plots/" directory.

Power BI Dashboard

An interactive dashboard was developed using Microsoft Power BI Desktop.

1. Sales Overview

This page presents an overview of sales performance, including:

- Total sales.
- Units sold.
- Order count.
- Average sales.
- Revenue by category.
- Monthly revenue trends.
- Interactive city, gender, and category slicers.

2. Transaction Details

This page displays the underlying sales transactions in a table.

Users can inspect order dates, customer information, cities, categories, products, quantities, and sales values.

3. Sales Analysis

This page provides additional visual analysis, including:

- Revenue by city.
- Revenue by product.
- Comparisons of sales performance across products and locations.

The dashboard helps users explore the dataset and identify important sales patterns.

Key Business Insights

The project helps answer the following business questions:

1. Which product categories generate the highest revenue?
2. Which cities contribute significantly to sales?
3. How does revenue change over time?
4. Which products perform well in terms of sales?
5. How many units have been sold?
6. How can interactive dashboards support business decision-making?

How to Run the Project

Step 1: Clone the Repository

git clone https://github.com/YOUR-USERNAME/ApexPlanet-Task3-Sales-Analytics-Dashboard.git

Replace "YOUR-USERNAME" with your GitHub username.

Step 2: Open the Project

Open the downloaded project folder in Visual Studio Code.

Step 3: Install Dependencies

pip install -r requirements.txt

Step 4: Run Data Cleaning

python src/clean_data.py

Step 5: Run Sales Analysis

python src/deep_dive_analysis.py

Step 6: Open the Power BI Dashboard

Open "ApexPlanet_Task3_Dashboard.pbix" using Microsoft Power BI Desktop.

If necessary, update the data source path to match the location of the project on your computer and refresh the data.

Project Deliverables

- Cleaned sales dataset.
- Python data cleaning script.
- Exploratory data analysis script.
- Generated sales analysis charts.
- Data quality report.
- Detailed analysis report.
- Interactive Power BI dashboard.

Conclusion

This project demonstrates the application of Python, Pandas, exploratory data analysis, and Power BI to transform raw sales data into meaningful business insights.

It helped me develop practical skills in data preparation, visualization, KPI analysis, and interactive dashboard development as part of my internship at ApexPlanet Software Pvt. Ltd.

Author

Shaik Shareef

Data Analytics Intern
ApexPlanet Software Pvt. Ltd.

Technologies Used

Python | Pandas | Power BI | Excel | SQL (where applicable) | Data Visualization

---

Project: ApexPlanet Task 3 — Sales Analytics Dashboard
