def cafe():
    snack=input(" Enter your order: ")

    if snack=="cookies" or snack=="samosa":
        print(f"Great Choice! We'll serve you {snack}")
        return "Thanks for ordering "
    
    else:
        return "Sorry,We only serve Cookies or Samosa with tea"
    
print(cafe())