seat_type=str(input("Enter your seat type (sleeper/AC/Luxury/General)")).lower()

match seat_type:
    case "sleeper":
        print("Sleeper:- No AC , Bed available")
    
    case "ac":
        print("AC:-Air-condition ,Bed with blankets")
    
    case "luxury":
        print("Luxury:- Perimium seats with Meal")

    case "general":
        print("General:- Seat is not confirm ")