#LIBRARY BOOK TRACKER
def available_books(library):
    
    available = []

    for title in library:

        total = library[title]["copies_total"]
        borrowed = library[title]["copies_borrowed"]

        if total - borrowed > 0:
            available.append(title)

    return available


def borrow_book(library, title):

    if title in library:

        total = library[title]["copies_total"]
        borrowed = library[title]["copies_borrowed"]

        if borrowed < total:
            library[title]["copies_borrowed"] = borrowed + 1
            print("Book borrowed.")
        else:
            print("Book is unavailable.")

    else:
        print("Book not found.")


def return_book(library, title):

    if title in library:

        if library[title]["copies_borrowed"] > 0:
            library[title]["copies_borrowed"] = library[title]["copies_borrowed"] - 1
            print("Book returned.")
        else:
            print("No borrowed copies.")

    else:
        print("Book not found.")


library = {
    "Python": {"copies_total": 3, "copies_borrowed": 2},
    "Java": {"copies_total": 2, "copies_borrowed": 2}
}

print(available_books(library))
borrow_book(library, "Python")
return_book(library, "Java")