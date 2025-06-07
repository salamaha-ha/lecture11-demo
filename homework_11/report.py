from .utils.formatting import format_book_list

def generate_report(library):
    books = library.list_books()
    if not books:
        return "В библиотеке нет книг."
    report = "Отчёт о книгах в библиотеке:\n"
    report += format_book_list(books)
    return report
