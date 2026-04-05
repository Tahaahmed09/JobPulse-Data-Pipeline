import requests
import os
from dotenv import load_dotenv
from utils.logger import logger
from utils.config import BASE_URL , url,  MAX_PAGES, PARAMS



def get_api_params():
    params = PARAMS.copy()
    load_dotenv()
    APP_ID = os.getenv('APP_ID')
    APP_KEY = os.getenv('APP_KEY')
    params["app_id"] = APP_ID
    params["app_key"] = APP_KEY
    return params



def extract_jobs(base_url):
    params = get_api_params()
    all_jobs = []

    for page in range (1,MAX_PAGES + 1):
        url = f'{base_url}/{page}' 

        logger.info(f"Fetching Page : {page}")

        response = requests.get(url, params=params)
        print(response.status_code)

        if response.status_code == 200:
            data = response.json()
            jobs = data["results"]

            all_jobs.extend(jobs)
            logger.info(f"Page : {page} Fetched, jobs : {len(jobs)}")

        else:
            logger.error(f"Error on page {page} {response.status_code}")
            break
    return all_jobs













# connecting with api and testing with one page

# def extract_jobs(url, params):
#     try:
#         logger.info(f"Requesting data from API: {url}")

#         response = requests.get(url, params=params)

#         if response.status_code == 200:
#             data = response.json()
#             logger.info(f"Data fetched successfully. Records: {len(data['results'])}")
#             return data['results']
#         else:
#             logger.error(f"API Error: {response.status_code}")
#             return []

#     except Exception as e:
#         logger.exception(f"Exception occurred during extraction: {e}")
#         return []
    



# Pagination (to extract multiple pages)






# jobs = extract_jobs(url,params)

# pagination = jobs_pagination(BASE_URL,params)

