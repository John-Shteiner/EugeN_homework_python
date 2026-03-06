def month_to_season(month):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Номер месяца должен быть от 1 до 12"

# Проверка работы функции
print(month_to_season(2))   # Ожидаем: Зима
print(month_to_season(5))   # Ожидаем: Весна
print(month_to_season(10))  # Ожидаем: Осень
