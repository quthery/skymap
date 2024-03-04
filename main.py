import random
import time
import math


map_width = 10 
map_height = 10  


num_stars = 3


stars = [(random.randint(0, map_width - 1), random.randint(0, map_height - 1)) for _ in range(num_stars)]


map_with_stars = [["." for _ in range(map_width)] for _ in range(map_height)]
for star in stars:
    x, y = star
    map_with_stars[y][x] = "*"


def print_map_with_stars(map_with_stars):
    for row in map_with_stars:
        print(" ".join(row))

# Функция для вычисления расстояния до звезд
def calculate_distances(user_x, user_y, stars):
    distances = []
    for star in stars:
        distance = math.sqrt((user_x - star[0]) ** 2 + (user_y - star[1]) ** 2)
        distances.append(distance)
    return distances


while True:
    print("\nNew exploration cycle started!")
    print_map_with_stars(map_with_stars)

    # Ввод координат пользователя
    user_input_x = input("\nEnter X coordinate (or type 'exit' to quit): ")
    if user_input_x.lower() == "exit":
        break
    user_input_x = int(user_input_x)
    user_input_y = int(input("Enter Y coordinate: "))

    distances = calculate_distances(user_input_x, user_input_y, stars)


    for i, distance in enumerate(distances):
        if distance == 0:
            print("You found a star!")
            stars[i] = (-1, -1)  


    for i, star in enumerate(stars):
        if star == (-1, -1):
            map_with_stars[user_input_y][user_input_x] = "!"  # Обозначаем место найденной звезды
            print_map_with_stars(map_with_stars)
            stars.pop(i)

    if not stars:
        print("All stars founded!")
        finish_exploration = input("\nFinish exploration? (y/n): ")
        if finish_exploration.lower() == "y":
            break


    print("\nDistances to stars:")
    for i, distance in enumerate(distances):
        if distance == 0:
            print("Founded")
        else:
            print("Distance to star {}: {:.2f} a.e.".format(i + 1, distance))
