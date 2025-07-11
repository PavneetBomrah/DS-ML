import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='library_db'
)
cursor = conn.cursor()

def addBook():
    title = input("Enter the title for the book: ")
    author = input("Enter the author for the book: ")
    cursor.execute("INSERT INTO books (author,title) VALUES (%s,%s);",(author,title))
    conn.commit()
    print("Book Added")

def renameBook():
    view_books()
    book_id = input("Enter Book ID to rename: ")
    new_title = input("New title: ")
    cursor.execute("UPDATE books SET title=%s WHERE id=%s", (new_title, book_id))
    conn.commit()
    print("Title updated")

def removeBook():
    view_books()
    book_id = input("Enter Book ID to remove: ")
    cursor.execute("DELETE FROM books WHERE id=%s", (book_id,))
    conn.commit()
    print("Book removed")

def viewBooks():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    print("\nBook List:")
    if not books:
        print("No books found.")
        return
    for b in books:
        status = "Yes" if b[3] else "No"
        print(f"ID: {b[0]} | Title: {b[1]} | Author: {b[2]} | Available: {status}")

def issueBook():
    viewBooks()
    book_id = input("Enter Book ID to issue: ")
    cursor.execute("SELECT available FROM books WHERE id=%s", (book_id,))
    result = cursor.fetchone()
    if result and result[0]:
        cursor.execute("UPDATE books SET available=0 WHERE id=%s", (book_id,))
        conn.commit()
        print(f"Book ID {book_id} issued to {user}.\n")
    else:
        print(" Book is not available.\n")

def returnBook():
    viewBooks()
    book_id = input("Enter Book ID to return: ")
    cursor.execute("SELECT available FROM books WHERE id=%s", (book_id,))
    result = cursor.fetchone()
    if result and not result[0]:
        cursor.execute("UPDATE books SET available=1 WHERE id=%s", (book_id,))
        conn.commit()
        print(f"Book ID {book_id} returned by {user}.\n")
    else:
        print("That book wasn't issued.\n")

def adminMenu():
    while True:
        print("ADMIN MENU")
        print("1. Add Book")
        print("2. View Books")
        print("3. Rename Book")
        print("4. Remove Book")
        print("0. Exit")

        choice = input("Choice: ")
        match choice:
            case "1": addBook()
            case "2": viewBooks()
            case "3": renameBook()
            case "4": removeBook()
            case "0":
                print("Logged out.")
                break
            case _: print("Invalid option.\n")

def userMenu():
    while True:
        print("USER MENU")
        print("1. View Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("0. Exit")

        choice = input("Choice: ")
        match choice:
            case "1": viewBooks()
            case "2": issueBook()
            case "3": returnBook()
            case "0":
                print("Logged out.")
                break
            case _: print("Invalid option.\n")

def login():
    print("---Welcome to Library---")
    user = input("Enter Username: ")
    if user == "admin":
        password = input("Enter Password: ")
        if password == "admin@123":
            adminMenu()
    else:
        userMenu()

login()
        