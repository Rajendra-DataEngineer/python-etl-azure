# 🐍 Python ETL Pipeline — Azure Blob Storage

## 📌 Project Overview
A Python-based ETL pipeline that extracts raw orders data from a CSV file,
transforms it using pandas, and loads the cleaned data into Azure Blob Storage.

---

## 🏗️ Architecture

Raw CSV → Extract → Transform → Load → Azure Blob Storage

---

## ⚙️ Tech Stack
- Python 3.14
- pandas
- azure-storage-blob
- python-dotenv
- Azure Blob Storage

---

## 🔄 ETL Steps

### Extract
- Reads raw `orders.csv` from local `data/` folder
- Logs row count on load

### Transform
- Drops rows with missing values
- Removes duplicate records
- Converts `OrderDate` to datetime format
- Adds `TotalAmount` column (Quantity × Price)
- Adds `LoadDate` column (today's date)

### Load
- Saves transformed CSV locally
- Uploads to Azure Blob Storage container `etl-output`
- Full logging at every step

---

## 📁 Project Structure

```
python-etl-azure/
│
├── data/
│   └── orders.csv              # Raw input data
├── etl/
│   └── etl_pipeline.py         # Main ETL script
├── logs/                       # Auto-generated log files
├── .env                        # Azure credentials (not pushed to GitHub)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

1. Clone the repo
2. Install dependencies:
```
pip install -r requirements.txt
```

3. Add your Azure credentials to `.env`:
```
AZURE_CONNECTION_STRING=your_connection_string
AZURE_CONTAINER_NAME=etl-output
```

4. Run the pipeline:
```
python etl/etl_pipeline.py
```

---

## 📊 Sample Output
| OrderID | CustomerID | ProductID | Quantity | Price | OrderDate | TotalAmount | LoadDate |
|---------|------------|-----------|----------|-------|-----------|-------------|----------|
| 1001 | C001 | P001 | 2 | 500 | 2026-01-01 | 1000 | 2026-06-03 |
| 1002 | C002 | P002 | 1 | 1000 | 2026-01-02 | 1000 | 2026-06-03 |

---

## ☁️ Azure Blob Storage Output
Transformed file uploaded to: `etl-output/transformed_orders.csv`

![Azure Blob Output]

<img width="797" height="390" alt="image" src="https://github.com/user-attachments/assets/e280d0f4-bddd-4156-8a21-15b536191905" />






Made by Rajendra K

Aspiring Azure Data Engineer | Open to UK Relocation
