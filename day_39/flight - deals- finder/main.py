from pprint import pprint

from flight_search import FlightSearch
from data_manager import DataManager
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# flight_search = FlightSearch() working with token
data_menger = DataManager()
flight_search = FlightSearch()

global_token = flight_search.token

data_menger.enter_test_in_all_row()
