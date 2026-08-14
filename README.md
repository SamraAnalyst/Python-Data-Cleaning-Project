# 🐍 Python Data Cleaning & Preprocessing Project

This repository demonstrates a clean and automated data preprocessing pipeline built using Python and the **Pandas** library. 

## 🛠️ Project Workflow
1. **Data Ingestion:** Loaded raw corporate sales data (`sales_data.csv`) into a Pandas DataFrame.
2. **Missing Value Analysis:** Identified structural gaps and unallocated entries using `.isnull().sum()`.
3. **Imputation:** Automated data filling for empty quantity metric records using conditional `.fillna()` operations.
4. **Deduplication:** Isolated and removed duplicate transactions with `.drop_duplicates()` to maintain data integrity.
5. **Pipeline Output:** Exported the verified, structured dataset into a pristine deployment-ready format (`cleaned_sales_data.csv`).

## 💻 Tech Stack Used
* **Language:** Python 3
* **Libraries:** Pandas
* **IDE:** Python IDLE
