stop_words = "абв"

# Строка со стоп-словами
string_to_process = "абвгдейка - это передача"

# lambda-функция, фильтрующая стоп-слова
split_str = string_to_process.split()
filtered_str = ' '.join((filter(lambda s: stop_words not in s, split_str)))

print("Отфильтрованная строка: ", filtered_str)