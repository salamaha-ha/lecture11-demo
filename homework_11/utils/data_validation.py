def validate_book_data(book):
    """
    Проверяет, что книга содержит корректные поля: title, author, genre (все строки, не пустые)
    """
    if not isinstance(book, dict):
        return False
    for key in ["title", "author", "genre"]:
        if key not in book or not isinstance(book[key], str) or not book[key].strip():
            return False
    return True
