#1
import math
R=float(input("Введите радиус в сантиметрах: \n"))
L=2*R*math.pi
S=math.pi*(R ** 2)
print(f"Длина окружности равна: {L: .2f}")
print(f"Площадь круга равна: {S: .2f}")

#2
x=10
y=55
print(f"Значения переменных до замены: {x,y}")
x, y = y, x
print(f"Значения переменных после замены: {x,y}")

#3
import math
L=input("Введите длину в метрах \n")
L=float(L)
g=float(9.81)
T=2*math.pi*math.sqrt(L/g)
print(f"Период колебания маятника: {T: .2f}")