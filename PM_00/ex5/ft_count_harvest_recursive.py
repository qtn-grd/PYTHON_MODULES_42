def ft_count_harvest_recursive(day=1, goal=0):
    if goal == 0:
        goal = int(input("Days until harvest: "))

    if day < goal:
        print("Day", day)
        ft_count_harvest_recursive(day + 1, goal)

    else:
        print("Day", day)
        print("Harvest time!")
