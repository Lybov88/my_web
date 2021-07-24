# *** Работа с файлами ***

# вызов функции опен, создание файла в режиме записи
# f = open("test.txt", 'w')
# # метод записи
# f.write("hello world!")
# # обязательный метод закрытия файла
# f.close()

# контекстный менеджер
# with open("test.txt", 'w') as f:
#     # f.write("hi friends!!")
#     # f.write("\n")
#     # f.write("123456")
#     print('qwertt', file=f)
#     print('1234', file=f)
#     print(',mmfgh', file=f)

# Добавление записи
# with open("test.txt", 'a') as f:
#     f.writelines(["qwerty", "python", "12345678"])

# чтение всего файла
with open("test.txt", 'r') as f:
    text = f.read()
# print(text)

# чтение отдельных строк из файла
with open("test.txt") as f:
    text = f.readline()
    print(text)
    text = f.readline
    print(text)
