from homework_11 import Library, generate_report

lib = Library()
lib.add_book('1984', 'Джордж Оруэлл', 'антиутопия')
lib.add_book('Мастер и Маргарита', 'Михаил Булгаков', 'роман')
lib.add_book('Питон для детей', 'Д. Раш', 'учебник')

print('--- Все книги ---')
for b in lib.list_books():
    print(b)

print('\n--- Поиск по автору "Булгаков" ---')
for b in lib.find_books(author='Булгаков'):
    print(b)

print('\n--- Отчёт ---')
print(generate_report(lib))
