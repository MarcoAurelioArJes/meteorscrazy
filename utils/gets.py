import requests
import pandas as pd
from  datetime import datetime, timedelta


def get_asteroids_by_date(start_date=None, end_date=None, API_KEY="vUKEyppBObY9lqG1ALMj4ACX9Ff7rW4RyTnsjsiT" ):

        
    if start_date is None:
        start_date_str = datetime.now().strftime("%Y-%m-%d")
    else:
        start_date_str = start_date
        
    if end_date is None:
        data_inicio_obj = datetime.strptime(start_date_str, "%Y-%m-%d")
        data_final_str = (data_inicio_obj + timedelta(days=7)).strftime("%Y-%m-%d")
    else:
        data_final_str = end_date
 
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data


get_asteroids_by_date()