from datetime import datetime,timedelta
from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager


if datetime.now().weekday() == 1:
    flight_search = FlightSearch()
    flight_data = FlightData(flight_search.token)
    data_manager = DataManager(flight_data)
    data_manager.check_ata_status()              # first check there is no empty slots
    info = flight_search.search_price(data_manager) # info a list of messages
    notify = NotificationManager(info)
    notify.mail_sender()
