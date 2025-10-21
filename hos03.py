def add_book(book_list, book):
    book_list.append(book)
    print(f"Added book: {book}")

def remove_book(book_list, title):
    for book in book_list:
        if book[0] == title:
            book_list.remove(book)
            print(f"Removed book: {title}")
            return
    print("Book not found.")

def search_book(book_list, title):
    for book in book_list:
        if book[0] == title:
            print(f"Found book: {book}")
            return
    print("Book not found")

def convert_to_tuples(book_list):
    return [tuple(book) for book in book_list]

def convert_to_lists(tuple_list):
    return [list(book) for book in tuple_list]

books_list = [["To Kill a Mockingbird", "Harper Lee"], ["1984", "George Orwell"]]
books_tuples = convert_to_tuples(books_list)

books_list_modifiable = convert_to_lists(books_tuples)

add_book(books_list_modifiable, ["A Brief History of Time", "Stephen Hawking"])
remove_book(books_list_modifiable, "1984")
search_book(books_list_modifiable, "To Kill a Mockingbird")

print("Final books list:")
for book in books_list_modifiable:
    print(book)