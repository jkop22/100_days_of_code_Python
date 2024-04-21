def how_much_paint(width, height, coverage):
    total = (width * height) / coverage
    print(f"U will need {round(total)} packages of paint to do the job.")

how_much_paint(4, 2, 5)

# varianta i se vstupem od usera

width = int(input("Enter the width of the area: "))
height = int(input("Enter the height of the area: "))

def how_much_paint1(width, height, coverage):
    total = (width * height) / coverage
    print(f"U will need {round(total)} packages of paint to do the job.")

how_much_paint1(width, height, 5)