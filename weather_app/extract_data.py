import requests
import pandas as pd

latitude_st = "59.30"
longitude_st = "18.02"
latitude_gb = "57.70"
longitude_gb = "11.97"
latitude_ma = "59.33"
longitude_ma = "11.07"

städer = {
    "stockholm": {"latitude": latitude_st,
                "longitude": longitude_st},
    "göteborg": {"latitude": latitude_gb,
                "longitude": longitude_gb},
    "malmö": {"latitude": latitude_gb,
                "longitude": longitude_gb}
}

def get_weather_data(city):

    url = f"https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{städer[city]["longitude"]}/lat/{städer[city]["latitude"]}/data.json"

    headers = {
        "Accept": "application/json"
    }

    r = requests.get(url= url, headers= headers)
    r.raise_for_status()
    data = r.json()
    return data 
    
def create_dict(stad):
    data = get_weather_data(stad)
    degree_data = []
    time_data = []

    for time in data["timeSeries"]:
        for x in time["parameters"]:
            
            if x["name"] == "t":
                time_data.append(time["validTime"])
                degree_data.append(x["values"][0])

    dict_test = {
        "time": time_data[0:24],
        "degree": degree_data[0:24]
    }

    return pd.DataFrame(dict_test)

print(create_dict(stad= "göteborg"))


    