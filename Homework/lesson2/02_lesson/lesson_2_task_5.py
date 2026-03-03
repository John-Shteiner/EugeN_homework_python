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
        return "Неверный номер месяца (введите от 1 до 12)"


print("Месяц 2:", month_to_season(2))
print("Месяц 4:", month_to_season(4))
print("Месяц 7:", month_to_season(7))
print("Месяц 10:", month_to_season(10))
print("Месяц 13:", month_to_season(13))







