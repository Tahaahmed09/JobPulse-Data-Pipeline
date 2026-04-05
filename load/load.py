from sqlalchemy import create_engine
from sqlalchemy import text
from utils.logger import logger
from dotenv import load_dotenv
import os

load_dotenv()
user = os.getenv('user')
password = os.getenv('password')
server = os.getenv('server')
port = os.getenv('port')
from sqlalchemy import text

def load_to_postgres(df):
    # Connecting to postgreSQL
    engine = create_engine(f"postgresql://{user}:{password}@{server}:{port}/api_jobs")
    
    # 1. Total rows in DataFrame (Source count)
    total_source_rows = len(df)
    
    try:
        # Step A: Data to temp table
        df.to_sql(name='temp_jobs', con=engine, if_exists='append', index=False)
        logger.info(f"Step 1: {total_source_rows} rows loaded to temporary table.")

        # Step B: Upsert query
        upsert_query = text("""
            INSERT INTO jobs (title, description, location, company, salary_min, salary_max, avg_yearly_salary, avg_monthly_salary, posted_date, currency, skills)
            SELECT title, description, location, company, salary_min, salary_max, avg_yearly_salary, avg_monthly_salary, posted_date, currency, skills
            FROM temp_jobs
            ON CONFLICT (title, company, posted_date) 
            DO NOTHING;
        """)

        with engine.begin() as conn:
            # Step C: Execute and get inserted count
            result = conn.execute(upsert_query)
            inserted_rows = result.rowcount  
            
            # Step D: Calculate skipped rows
            skipped_rows = total_source_rows - inserted_rows

            # Step E: Cleanup
            conn.execute(text("TRUNCATE TABLE temp_jobs;"))

        # Step F: Final Logging
        logger.info(f"Success! Inserted: {inserted_rows} | Skipped (Duplicates): {skipped_rows} | Total Processed: {total_source_rows}")
        
    except Exception as e:
        logger.error(f"Loading Error: {str(e)}")