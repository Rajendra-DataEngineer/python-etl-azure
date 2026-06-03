# ============================================
# Python ETL Pipeline - Azure Blob Storage
# Author: Rajendra
# Description: Extract, Transform, Load orders data to Azure Blob Storage
# ============================================

import pandas as pd
import logging
import os
from datetime import datetime
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

# ── Setup Logging ──────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(f"logs/etl_log_{datetime.today().strftime('%Y%m%d')}.txt"),
        logging.StreamHandler()
    ]
)
log = logging.getLogger(__name__)

# ── Load Environment Variables ─────────────
load_dotenv()

# ============================================
# EXTRACT
# ============================================
def extract(filepath):
    log.info("Starting EXTRACT phase...")
    df = pd.read_csv(filepath)
    log.info(f"Loaded {len(df)} rows from {filepath}")
    return df

# ============================================
# TRANSFORM
# ============================================
def transform(df):
    log.info("Starting TRANSFORM phase...")
    original_count = len(df)

    # 1. Drop rows with missing values
    df = df.dropna()
    log.info(f"Dropped {original_count - len(df)} rows with missing values")

    # 2. Remove duplicate rows
    df = df.drop_duplicates()
    log.info(f"Removed duplicates. Rows remaining: {len(df)}")

    # 3. Convert OrderDate to datetime
    df["OrderDate"] = pd.to_datetime(df["OrderDate"])

    # 4. Add TotalAmount column
    df["TotalAmount"] = df["Quantity"] * df["Price"]
    log.info("Added TotalAmount column (Quantity x Price)")

    # 5. Add LoadDate column
    df["LoadDate"] = datetime.today().strftime("%Y-%m-%d")
    log.info("Added LoadDate column")

    log.info(f"Transform complete. Final row count: {len(df)}")
    return df

# ============================================
# LOAD
# ============================================
def load(df, filename):
    log.info("Starting LOAD phase...")

    # Save transformed file locally first
    output_path = f"data/transformed_{filename}"
    df.to_csv(output_path, index=False)
    log.info(f"Saved transformed file locally: {output_path}")

    # Upload to Azure Blob Storage
    conn_str = os.getenv("AZURE_CONNECTION_STRING")
    container = os.getenv("AZURE_CONTAINER_NAME")

    if not conn_str or not container:
        log.warning("Azure credentials not found in .env — skipping upload")
        return

    try:
        client = BlobServiceClient.from_connection_string(conn_str)
        blob_client = client.get_blob_client(container=container, blob=f"transformed_{filename}")
        with open(output_path, "rb") as f:
            blob_client.upload_blob(f, overwrite=True)
        log.info(f"Successfully uploaded to Azure Blob: {container}/transformed_{filename}")
    except Exception as e:
        log.error(f"Upload failed: {e}")

# ============================================
# MAIN
# ============================================
if __name__ == "__main__":
    log.info("========== ETL Pipeline Started ==========")
    raw_df = extract("data/orders.csv")
    transformed_df = transform(raw_df)
    load(transformed_df, "orders.csv")
    log.info("========== ETL Pipeline Completed ==========")