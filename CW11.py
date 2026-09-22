from tripdata import get_trip
from datetime import datetime
import json
trips = []
trip1 = get_trip("Kochi", "15-05-2023", "Visited Fort Kochi")
trip2 = get_trip("Munnar", "20-06-2023", "Enjoyed the beautiful hills")
trip3 = get_trip("Kozhikode", "10-07-2023", "Visited the beach")
trips.append(trip1)
trips.append(trip2)
trips.append(trip3)
for trip in trips:
    date_object = datetime.strptime(trip["date"], "%d-%m-%Y")
    trip["date"] = date_object.strftime("%B %d, %Y")

json_data = json.dumps(trips, indent=4)

print(json_data)