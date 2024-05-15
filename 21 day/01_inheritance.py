class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")

class Bird(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Most efficient of all vertebrates")

    def fly(self):
        print("Can move in air.")

tweety = Bird()
tweety.fly()
tweety.breathe()
print(tweety.num_eyes)

# slicing

week = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
work_days = week[:5]
print(work_days)
weekend = week[5:]  
print(weekend)
middle = week[2:5]
print(middle)

print(week[::2])        # každý druhý prvek se vynechá (vypíšou se liché prvky z listu)
print(week[1::2])       # vypíšou se sudé prvky z listu
print(week[::-1])       # výpis struktury v obráceném pořadí
print(week[2:5:2])      # vypíše pouze středu a pátek
