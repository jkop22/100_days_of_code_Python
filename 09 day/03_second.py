# nesting
# list in a dictionary
person = {
    "f_name": "Jan",
    "l_name": "Kopecny",
    "birthplace": "Bruntal",
    "hometown": "Ostrava",
    "languages": ["CZ", "EN","DE", "IT"],
    "drivers_licence": ["B", "C", "E"]
}
# dict in dict
person = {
    "f_name": "Jan",
    "l_name": "Kopecny",
    "birthplace": "Bruntal",
    "hometown": "Ostrava",
    "languages": ["CZ", "EN","DE", "IT"],
    "drivers_licence": ["B", "C", "E"],
    "previous_jobs": {
        "VSB": "IT spec and lecturer",
        "IBM": "Shift Lead",
        "Verizon": "Networking spec"
    }
}

print(person)
print(person["languages"][2])
print(person["previous_jobs"])

for i in person["languages"]:
    print(i)