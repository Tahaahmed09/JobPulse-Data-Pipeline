# 🚀 JobPulse Data Pipeline

A production-style **ETL Data Pipeline** that extracts job listings from an API, transforms the data, and loads it into a PostgreSQL database with proper logging, deduplication, and incremental loading logic.

---

## 📌 Project Overview

**JobPulse Data Pipeline** is designed to simulate a real-world **data engineering workflow**:

* 🔍 Extract job data from API (Adzuna)
* 🔄 Transform and clean raw JSON data
* 🧠 Extract insights like salary metrics & skills
* 💾 Load data into PostgreSQL using upsert logic
* 📝 Log every step for monitoring & debugging

---

## 🏗️ Project Structure

```id="x3j2h8"
JobPulse_Data_Pipeline/
│
├── extract/
│   └── api_extract.py          # API data extraction (pagination)
│
├── transform/
│   └── transform.py           # Data cleaning & feature engineering
│
├── load/
│   └── load.py                # Load data into PostgreSQL
│
├── utils/
│   ├── config.py              # Configurations (API, params)
│   └── logger.py              # Centralized logging system
│
├── main.py                    # Pipeline entry point
├── requirements.txt           # Dependencies
├── .gitignore                 # Ignored files
└── README.md
```

---

## ⚙️ Pipeline Workflow

### 1️⃣ Extract (API Layer)

* Fetches job listings using **Adzuna API**
* Implements **pagination**
* Handles API errors
* Logs each request

---

### 2️⃣ Transform (Data Processing)

* Cleans nested JSON fields (company, location)
* Filters relevant records
* Creates new features:

  * Average yearly salary
  * Monthly salary
  * Posting date
* Extracts skills from job descriptions:

  * Python, SQL, AWS, Airflow, Cloud
* Removes duplicate records

---

### 3️⃣ Load (Database Layer)

* Loads data into PostgreSQL
* Uses **temporary table + upsert logic**
* Avoids duplicates using:

```id="x7s8d2"
ON CONFLICT (title, company, posted_date) DO NOTHING
```

* Tracks:

  * Inserted rows
  * Skipped rows
  * Total processed rows

---

### 4️⃣ Logging

* Centralized logging system
* Logs stored in:

```id="c0v3x9"
etl.log
```

Example:

```id="p8j9k1"
2026-04-01 12:00:01 - INFO - Fetching Page : 1
2026-04-01 12:00:03 - INFO - Page : 1 Fetched, jobs : 50
2026-04-01 12:00:05 - INFO - Success! Inserted: 120 | Skipped: 30
```

---

## 🧪 Tech Stack

* Python 🐍
* Pandas
* Requests
* BeautifulSoup (optional scraping layer)
* SQLAlchemy
* PostgreSQL
* dotenv (environment variables)

---

## 🔐 Environment Variables

Create a `.env` file:

```id="q2l7s4"
APP_ID=your_api_id
APP_KEY=your_api_key

user=your_db_user
password=your_db_password
server=localhost
port=5432
```

---

## ▶️ How to Run

### 1️⃣ Clone Repository

```id="g1r8t5"
git clone https://github.com/your-username/JobPulse_Data_Pipeline.git
cd JobPulse_Data_Pipeline
```

---

### 2️⃣ Install Dependencies

```id="b9m2v7"
pip install -r requirements.txt
```

---

### 3️⃣ Setup PostgreSQL

* Create database:

```id="k5n1p3"
CREATE DATABASE api_jobs;
```

* Create table:

```id="h8d4l6"
CREATE TABLE jobs (
    title TEXT,
    description TEXT,
    location TEXT,
    company TEXT,
    salary_min FLOAT,
    salary_max FLOAT,
    avg_yearly_salary FLOAT,
    avg_monthly_salary FLOAT,
    posted_date DATE,
    currency TEXT,
    skills TEXT,
    PRIMARY KEY (title, company, posted_date)
);
```

---

### 4️⃣ Run Pipeline

```id="r7f2y9"
python main.py
```

---

## 📊 Features

✔ API-based data ingestion
✔ Pagination handling
✔ Data cleaning & feature engineering
✔ Skill extraction from text
✔ Deduplication logic
✔ Incremental loading (Upsert)
✔ Logging (file + console)

---

## 💡 Key Learnings

* Building scalable ETL pipelines
* Working with APIs in production scenarios
* Handling structured + unstructured data
* Database optimization using upsert
* Logging for monitoring pipelines

---

## 🚀 Future Improvements

* Add Airflow for scheduling
* Store raw data in data lake (S3)
* Add Docker support
* Implement data validation layer
* Build dashboard (Power BI / Tableau)

---

## 👨‍💻 Author

Taha Ahmed

---

⭐ If you find this project useful, consider giving it a star!
