def chai_stall():
    size= input("Choose your cup size (Small/Medium/Large): ").lower()

    if size=="small":
        print(f"{size}: cup is 10 rupees")

    elif size=="medium":
         print(f"{size}: cup is 15 rupees")

    elif size=="large":
         print(f"{size}: cup is 20 rupees")
    else:
        print(f"{size} cup is unavailable.")

chai_stall()

