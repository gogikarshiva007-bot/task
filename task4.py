library = {}

def add_book():
    book_id = input("Enter book ID: ")
    title = input("Title: ")
    author = input("Author: ")
    year = int(input("Year: "))
    library[book_id] = {
        "title": title,
        "author": author,
        "year": year
    }

def remove_book():
    book_id = input("Enter book ID to remove: ")
    library.pop(book_id, "Book not found")

def search_book():
    title = input("Enter title to search: ")
    for book in library.values():
        if book["title"].lower() == title.lower():
            print(book)

def update_book():
    book_id = input("Enter book ID to update: ")
    if book_id in library:
        library[book_id]["title"] = input("New title: ")
        library[book_id]["author"] = input("New author: ")
        library[book_id]["year"] = int(input("New year: "))

def report():
    print("Total books:", len(library))
    for book in library.values():
        print(book)

while True:
    print("\n1.Add 2.Remove 3.Search 4.Update 5.Report 6.Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        update_book()
    elif choice == "5":
        report()
    elif choice == "6":
        break
