from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Countries", ["Czechia", "Poland", "Germany", "Austria"])
table.add_column("Capital", ["Praha", "warszawa", "Berlin", "Wien"])

table.align = "l"

print(table)

