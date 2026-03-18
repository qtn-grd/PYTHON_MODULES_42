def ft_water_reminder():
    delay = int(input("Days since last watering: "))
    if delay > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
