def ft_count_harvest_recursive(count=1, goal=None):

    if not goal:
        goal = int(input("Day until harvest: "))

    if count <= goal:
        print(f"Day = {count}")
        count += 1
        ft_count_harvest_recursive(count, goal)

    else:
        print("Harvest time!")
