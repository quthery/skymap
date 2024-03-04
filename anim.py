import random
import time

# Рисунок звезды символами ASCII с внутренним текстом "Python"
star_art = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄⠄⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠄⠄⠄⠄⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠁⠄⠄⠄⠄⠄⠈⠛⠛⠛⠛⠛⠛⠛⠛⠛⣻ 
⣿⣿⣦⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣴⣿⣿⣿ 
⣿⣿⣿⣿⣷⣦⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣴⣾⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⣷⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⣾⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄⠄⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⡿⠁⠄⠄⠄⣠⣤⣶⣤⣄⠄⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⠃⠄⢀⣠⣾⣿⣿⣿⣿⣿⣷⣄⡀⠄⠘⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⢏⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⡹⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿сosmyQuest.gg⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

"""

# Координаты объекта (допустим, представим, что это координаты в трехмерном пространстве)
object_x = 50
object_y = 30
object_z = 20

# Функция для расчета расстояния до объекта
def calculate_distance(x, y, z, object_x, object_y, object_z):
    distance = ((x - object_x) ** 2 + (y - object_y) ** 2 + (z - object_z) ** 2) ** 0.5
    return distance

# Генерация случайных координат пользователя
user_x = random.randint(0, 100)
user_y = random.randint(0, 100)
user_z = random.randint(0, 100)

# Ввод пользователя для координат
user_input_x = int(input("Enter the X coordinate: "))
user_input_y = int(input("Enter the Y coordinate: "))
user_input_z = int(input("Enter the Z coordinate: "))

# Вывод рисунка звезды с текстом "Python"
print(star_art)

# Анимация сканирования
print("Scanning for object coordinates...", end="", flush=True)
for _ in range(5):
    time.sleep(0.5)
    print(".", end="", flush=True)
print()

# Расчет расстояния до объекта
distance = calculate_distance(user_input_x, user_input_y, user_input_z, object_x, object_y, object_z)

# Вывод результата на русском языке
if distance <= 10:
    print("Вы угадали! Вы нашли объект!")
else:
    print("Вы не угадали. Расстояние до объекта составляет {:.2f} условных метров.".format(distance))

