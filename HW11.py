from tracker import create_record
from datetime import datetime
import json

records = []

records.append(create_record("Kochi", "Visited Fort Kochi", "05-06-2022"))
records.append(create_record("Munnar", "Enjoyed the hills", "15-07-2022"))
records.append(create_record("Kozhikode", "Visited the beach", "20-08-2022"))

for record in records:
    date_object = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_object.strftime("%B %d, %Y")

json_data = json.dumps(records)

print("JSON Data:")
print(json_data)

data = json.loads(json_data)

print("\nTravel Records:")

for record in data:
    print(record)
  