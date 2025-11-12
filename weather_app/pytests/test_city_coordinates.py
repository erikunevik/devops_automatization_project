import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from extract_data import städer

# Pytest asserting that the coordinates for the three cities are correct
def testing_city_coordinates():
    
    assert (städer["stockholm"]["latitude"], städer["stockholm"]["longitude"])  == ("59.30", "18.02")
    assert (städer["göteborg"]["latitude"], städer["göteborg"]["longitude"])  == ("57.70", "11.97")
    assert (städer["malmö"]["latitude"], städer["malmö"]["longitude"])  == ("59.33", "11.07")
    
    
