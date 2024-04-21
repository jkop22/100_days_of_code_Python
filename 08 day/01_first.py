# repte k zakladním funkcim
# definovat simple fci se třemi printy a zavolat

def repte_func():
    print("Hello")
    print("From")
    print("Function\n")

print("Lets call the function:")
repte_func()

# fce s parametrem

def greeting(name):
    print(f"Hello {name.capitalize()}")
    print("From Function\n")

greeting("honza")
greeting("Majkl")

# fce s více parametry

def hello_person(name, hometown):
    print(f"Hello {name} from {hometown}.\n")

hello_person("Jan", "Ostrava")
hello_person(hometown="Ostrava", name="Jan")

