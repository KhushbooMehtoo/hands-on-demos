course =["Python development","Gen AI in Python","Data science"]
price=[50000,70000,90000]

for courses,prices in zip(course,price):
    print(f"{courses} in {prices}/-")