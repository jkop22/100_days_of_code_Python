travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, num_of_visits, cities):
    new_entry = {}
    new_entry["country"] = country
    new_entry["visits"] = num_of_visits
    new_entry["cities"] = cities
    travel_log.append(new_entry)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)