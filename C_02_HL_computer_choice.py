import random

high = int(input("High: "))
low = int(input("Low: "))

for item in range(0, 30):
    comp_choice = random.randint(low, high)
    print(comp_choice, end="\t")
