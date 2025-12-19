def cafe():
    snack=input(" Enter your order: ")

    if snack=="cokies" or snack=="smosa":
        print(f"Great Choice! We'll serve you {snack}")
        return "Thanks for ordering "
    
    else:
        return "Sorry its not available"
    
print(cafe())