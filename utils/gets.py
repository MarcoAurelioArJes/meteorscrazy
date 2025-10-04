import requests
import pandas as pd
from datetime import datetime, timedelta


def get_asteroids_by_date(start_date=None, end_date=None, API_KEY="vUKEyppBObY9lqG1ALMj4ACX9Ff7rW4RyTnsjsiT" ):
    
    # 1. TRATA DATA DE INÍCIO
    if start_date is None:
        # Define start_date_str como a data atual no formato string
        start_date_str = datetime.now().strftime("%Y-%m-%d")
    else:
        # Usa o valor fornecido
        start_date_str = start_date
        
    # 2. TRATA DATA FINAL
    if end_date is None:
        # a) Converte a string start_date_str para objeto datetime
        data_inicio_obj = datetime.strptime(start_date_str, "%Y-%m-%d")
        
        # b) Soma 7 dias ao objeto datetime e formata o resultado para string
        data_final_str = (data_inicio_obj + timedelta(days=7)).strftime("%Y-%m-%d")
    else:
        # Usa o valor fornecido para a data final
        data_final_str = end_date
    
    # 3. CONSTRUÇÃO DA URL (Usando as variáveis *_str)
    # Correção: Use start_date_str e data_final_str, que são as variáveis válidas.
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date_str}&end_date={data_final_str}&api_key={API_KEY}"
    
    response = requests.get(url)
    
    response.raise_for_status() 
    
    data = response.json()
    return data


data = get_asteroids_by_date()
print("Dados recebidos da NASA:")
print(data)