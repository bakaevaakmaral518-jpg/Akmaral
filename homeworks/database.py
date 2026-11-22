import sqlite3
connection = sqlite3.connect("books.db")


def create_table():
    connection.execute("""
     CREATE TABLE IF NOT EXISTS books (
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    """)
    connection.commit()

def insert_books(books):
    for book in books:
        connection.execute(
            "INSERT INTO books VALUES (?, ?, ?, ?, ?, ?)",
        book
        )
        connection.commit()

if __name__ == '__main__':
    create_table()

    books = [
        ("Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман", 480, 5),
        ("Война и мир", "Лев Толстой", 1869, "Роман", 1300, 4),
        ("Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", 672, 3),
        ("Евгений Онегин", "Александр Пушкин", 1833, "Роман", 224, 6),
        ("Отцы и дети", "Иван Тургенев", 1862, "Роман", 288, 4),
        ("Герой нашего времени", "Михаил Лермонтов", 1840, "Роман", 192, 3),
        ("Анна Каренина", "Лев Толстой", 1877, "Роман", 864, 2),
        ("Идиот", "Фёдор Достоевский", 1869, "Роман", 640, 3),
        ("Капитанская дочка", "Александр Пушкин", 1836, "Повесть", 160, 5),
        ("Тихий Дон", "Михаил Шолохов", 1940, "Роман", 1500, 2)
    ]

    insert_books(books)

    connection.close()

