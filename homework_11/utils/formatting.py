def format_book_list(books):
    lines = []
    for idx, book in enumerate(books, 1):
        lines.append(f"{idx}. {book['title']} — {book['author']} [{book['genre']}]")
    return '\n'.join(lines)
