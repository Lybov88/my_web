# *** Работа с файлами ***

# создание файла в режиме записи
# f = open("test.txt", 'w')
# # метод записи
# f.write("hello world")
# # обязательный метод закрытия файла
# f.close()

# контекстный менеджер
# with open("test.txt", 'w') as f:
# 	# f.write("python")
# 	# f.write("\n")
# 	# f.write("1234")
# 	print("qwerty", file=f)
# 	print("124232", file=f)
# 	print("hrthr", file=f)

# добавление записи
# with open("test.txt", 'a') as f:
# 	f.writelines(["qwerty", "python", "12345"])

# чтение всего файла
# with open("test.txt") as f:
# 	text = f.read()

# print(text)

# чтение отдельных строк из файла
with open("test.txt") as f:
	text = f.readline()
	print(text)
	text = f.readline()
	print(text)