# *** Исключения (исключительные события) ***
# Пример ошибки "деление на ноль"
a = 100
b = 0

# без обоаботки исключений
# c = a / b


# с обработкой исключения
# try:
#     # потенциально аварийный код
#     c = a / b
# except:
#         # "запасной код, срабатывающий при исключениях"
#         c = 0
# print(c)

# обработка конкретных исключений
b = 10

try:
    # потенциально аварийный код
    c = a / b
except ZeroDivisionError as err:
    print(f"Попытка деления на ноль. Ошибка: {err}")
except ValueError as err:
    print(f"Не число. Ошибка: {err}")
except TypeError as err:
    print(f"Ошибка в типе. Ошибка: {err}")
except Exception as err:
    print(f"Чтото пошло не так. Ошибка: {err}")
finally:
    print("Сработало finally")
