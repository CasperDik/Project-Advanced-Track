def distance():
    while True:
        try:
            distance = float(input(("How far are you planning to travel in km? ")))
            if distance < 0:
                raise ValueError
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    return distance

def travel_time(travel_speed, km):
    travel_time_hours = km / travel_speed
    travel_time_minutes = travel_time_hours * 60
    print("estimated travel time in hours: ", travel_time_hours)
    print("estimated travel time in minutes: ", travel_time_minutes)

def bike():
    km = distance()
    travel_speed = 15  #km/h
    travel_time(travel_speed, km)

def car():
    km = distance()
    travel_speed = 80  #km/h
    travel_time(travel_speed, km)

def walking():
    km = distance()
    travel_speed = 5  #km/h
    travel_time(travel_speed, km)

bike()