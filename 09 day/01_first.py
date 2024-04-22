# dictionary basics
# create a dictionary
person = {
    "f_name": "Jan",
    "l_name": "Kopecny",
    "birthplace": "Bruntal",
    "hometown": "Ostrava"
}
# use values from it
print(f"{person["f_name"]} {person["l_name"]} was born in {person["birthplace"]} and now lives in {person["hometown"]}.")
# add new key-value pair to dictionary
person["age"] = 43
# use this new value
print(f"And he is {person["age"]} years old.")
# new empty dict
new_dict = {}
# erase entries in existing dict
print(person)
# person = {}
print(person)
# loop over dict 1 / prints out key names
for item in person:
    print(item)
# loop over dict 2 / prints key and then its value
for key in person:
    print(key)
    print(person[key])