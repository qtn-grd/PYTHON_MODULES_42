def ft_count_harvest_iterative():
    goal = int(input("Days until harvest: "))
    for day in range(1, goal + 1):
        print("Day", day)
    print("Harvest time!")
