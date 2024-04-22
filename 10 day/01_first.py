# functions with output basics

def multiply(input1, input2):
    return input1 * input2

print(multiply(3,4))

output = multiply(3,4)
print(output)

# formatovani stringu

def format_name(f_name, l_name):
    full_name_formated = l_name.capitalize() + " " + f_name.capitalize()
    return full_name_formated

first1 = "JAN"
last1 = "kopecny"

result = format_name(first1, last1)
print(result)

# return jako odchod z funkce

def format_name2(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Parameter(s) missing..."
    full_name_formated = l_name.capitalize() + " " + f_name.capitalize()
    return full_name_formated

first2 = input("Enter first name: ")
last2 = input("Enter last name: ")

print(format_name2(first2, last2))


