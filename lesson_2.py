#1
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
try:
    result = a / b
    print(f'Результат деления {a} на {b}: {result}')
except ZeroDivisionError:
    print("Ошибка! Деление на ноль невозможно.")

#2
def calculate_discounted_price(total_amount):
    if total_amount > 20:
        discount_percentage = 0.35
        discount_amount = total_amount * discount_percentage
        discounted_price = total_amount - discount_amount
        return round(discounted_price, 2), round(discount_amount, 2)
    else:
        return total_amount, 0
total_amount = float(input("Введите сумму покупки: "))
final_price, discount = calculate_discounted_price(total_amount)
print(f"Итоговая стоимость: {final_price:.2f}")
if discount != 0:
    print(f"Скидка составила: {discount:.2f}")
else:
    print("Скидка не предоставлена")

#3
months = {
    1: ("Январь", "Зима"),
    2: ("Февраль", "Зима"),
    3: ("Март", "Весна"),
    4: ("Апрель", "Весна"),
    5: ("Май", "Весна"),
    6: ("Июнь", "Лето"),
    7: ("Июль", "Лето"),
    8: ("Август", "Лето"),
    9: ("Сентябрь", "Осень"),
    10: ("Октябрь", "Осень"),
    11: ("Ноябрь", "Осень"),
    12: ("Декабрь", "Зима")
}
month_number = int(input("Введите номер месяца (от 1 до 12): "))
if month_number in months:
    month_name, season = months[month_number]
    print(f"{month_name} - это {season}.")
else:
    print("Недопустимый номер месяца. Попробуйте еще раз.")