import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from extract_data import städer
import pytest

# Asserting that the API respods succesfully to my request / i.e. 200


@pytest.mark.parametrize("city", ["stockholm", "göteborg", "malmö"]) # Decorator for testing the different cities 
    
def test_api_response(city):
    
    url = f"https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{städer[city]['longitude']}/lat/{städer[city]['latitude']}/data.json"
    
    headers = {
    "Accept": "application/json"
    }
    
    r = requests.get(url= url, headers= headers)

    assert r.status_code == 200
    
    

    
    

    
    