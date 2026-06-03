# ⚡ PySpark Sales Analytics Pipeline — Databricks

## 📌 Project Overview
A PySpark-based Sales Analytics Pipeline built on Databricks using the 
Medallion Architecture (Bronze → Silver → Gold) with Delta Lake tables.

---

## 🏗️ Architecture
Raw Data → Bronze Layer → Silver Layer → Gold Layer → Delta Tables

## ⚙️ Tech Stack
- Python / PySpark
- Databricks (Serverless)
- Delta Lake
- Medallion Architecture

---

## 🔄 Pipeline Layers

### 🥉 Bronze Layer
- Loads raw sales data with 15 rows
- Contains intentional dirty data (NULL values)

### 🥈 Silver Layer
- Drops NULL rows (15 → 13 clean rows)
- Converts OrderDate to date format
- Adds TotalAmount column (Quantity × Price)

### 🥇 Gold Layer
- **Customer Sales:** Total sales, orders, avg order value per customer
- **Product Revenue:** Top products ranked by revenue
- **Monthly Trend:** Sales aggregated by month and year

---

## 📊 Sample Analytics Output

### Total Sales by Customer
| CustomerID | TotalSales | TotalOrders | AvgOrderValue |
|------------|------------|-------------|---------------|
| C001 | 6250.0 | 3 | 2083.33 |
| C005 | 6000.0 | 3 | 2000.0 |
| C004 | 3750.0 | 2 | 1875.0 |

### Monthly Sales Trend
| Year | Month | MonthlySales |
|------|-------|--------------|
| 2026 | 1 | 12750.0 |
| 2026 | 2 | 8500.0 |

---

## 🚀 How to Run
1. Import the `.ipynb` notebook into Databricks
2. Attach to a cluster or Serverless compute
3. Run all cells top to bottom

---

## 🗄️ Delta Tables Created
- `silver_orders` — Cleaned orders data
- `gold_customer_sales` — Sales aggregated by customer
- `gold_product_sales` — Revenue aggregated by product
- `gold_monthly_trend` — Sales aggregated by month