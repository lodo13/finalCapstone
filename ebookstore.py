"""importing modules and opening the database file."""
import sys
import sqlite3
db = sqlite3.connect('ebookstore.db')
cursor = db.cursor()


def newbook():
    """it creates a new book in the database."""
    title = input("Enter book name: ").title()
    author = input("Enter author: ").title()
    while True:
        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Please enter a correct quantity.")
            continue
        break
    db = sqlite3.connect('ebookstore.db')
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO books(title, author, qty) VALUES(?,?,?)", (title, author, quantity))
    db.commit()
    db.close()
    print("Book added.")


def updatebook():
    """it updates a book in the database."""
    sel = input("""What would you like to update? 
    1. Title
    2. Author
    3. Quantity
    :""")
    if sel == "1":
        chosen = input("Enter book id: ")
        new_title = input("Enter new title: ").title()
        db = sqlite3.connect('ebookstore.db')
        cursor = db.cursor()
        cursor.execute("UPDATE books SET title=? WHERE id=?",
                       (new_title, chosen))
        db.commit()
        db.close()
        print("Book updated.")
    elif sel == "2":
        chosen = input("Enter book id: ")
        new_author = input("Enter new author: ").title()
        db = sqlite3.connect('ebookstore.db')
        cursor = db.cursor()
        cursor.execute("UPDATE books SET author=? WHERE id=?",
                       (new_author, chosen))
        db.commit()
        db.close()
        print("Book updated.")
    elif sel == "3":
        chosen = input("Enter book id: ")
        new_qty = int(input("Enter new quantity: "))
        db = sqlite3.connect('ebookstore.db')
        cursor = db.cursor()
        cursor.execute("UPDATE books SET qty=? WHERE id=?", (new_qty, chosen))
        db.commit()
        db.close()
        print("Book updated.")
    else:
        print("Invalid option.")


def deletebook(id):
    """it deletes a book from the database."""
    db = sqlite3.connect('ebookstore.db')
    cursor = db.cursor()
    cursor.execute("DELETE FROM books WHERE id =?", (id,))
    db.commit()
    db.close()
    print("Book deleted.")


def searchbook():
    """it searches a book in the database."""
    db = sqlite3.connect('ebookstore.db')
    cursor = db.cursor()
    sel = input("""Would you like to search by: 
    1. Author 
    2. Title? 
    :""")
    if sel == "1":
        authorbook = input("Enter author: ")
        cursor.execute(
            'SELECT * FROM books WHERE author LIKE "%{}%"'.format(authorbook))
        for row in cursor.fetchall():
            print(row)
    elif sel == "2":
        titlebook = input("Enter title: ")
        cursor.execute(
            'SELECT * FROM books WHERE title like "%{}%"'.format(titlebook))
        for row in cursor.fetchall():
            print(row)
    else:
        print("Invalid option.")


"""creates the table in the database if it's not existing"""
cursor.execute(
    """create table if not exists books (id integer primary key autoincrement, title text, author text, qty integer)""")

"""it adds the first books into the database"""
try:
    cursor.execute("""insert into books (id, title, author, qty) values (3001, "A Tale of Two Cities", "Charles Dickens", 30),
(3002, "Harry Potter and the Philosopher's Stone ", "J.K. Rowling", 40),
(3003, "The Lion, the Witch and the Wardrobe", "C. S. Lewis", 25),
(3004, "The Lord of the Rings", "J. R. R. Tolkien", 37), 
(3005, "Alice in Wonderland", "Lewis Carroll", 12)""")

except sqlite3.IntegrityError as e:
    pass

finally:
    db.commit()
    db.close()

"""menu"""
while True:
    select = input("""Select option: 
    """
                   """
    1. New book
    2. Update book
    3. Delete book
    4. Search book
    5. Show all books
    0. Exit
    
    :""")

    if select == "1":
        newbook()
        continue
    elif select == "2":
        updatebook()
        continue
    elif select == "3":
        deletebook(input("Enter id: "))
        continue

    elif select == "4":
        searchbook()
        continue

    elif select == "0":
        print("Goodbye!")
        sys.exit()

    elif select == "5":
        db = sqlite3.connect('ebookstore.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM books")
        for row in cursor.fetchall():
            print(row)
        continue

    else:
        print("Invalid option.")
        continue
