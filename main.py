from extract.api_extract import extract_jobs
from transform.transform_job import transform_jobs 
from utils.config import BASE_URL
from load.load import load_to_postgres

raw_data = extract_jobs(BASE_URL)

df = transform_jobs(raw_data)

load_to_postgres(df)






