#A (3,6); B (2,1) -> 5,09
#A (7,-5); B (1,-1) -> 7,21

print("Введите координаты точки А:")
x_A = float(input("Координата X:"))
y_A = float(input("Координата Y:"))
print("Введите координаты точки B:")
x_B = float(input("Координата X:"))
y_B = float(input("Координата Y:"))
import math
sqrt = round(math.sqrt((x_A - x_B) ** 2 + (y_A - y_B) ** 2),3)
print('Расстояние между точками =' , sqrt)