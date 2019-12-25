import sqlite3

def insert_books():
    conn = sqlite3.connect("my_books.db")
    cur = conn.cursor()

    insert_sql = "insert into my_books values (?, ?, ?, ?, ?)"
    cur.execute(insert_sql, ('개발자의 코드', '2013.02.28', 'A', 200, 0))

    books = [
        ('빅데이터 마케팅', '2013.02.28', 'A', 200, 1),
        ('구글드', '2013.02.10', 'B', 526, 0),
        ('강의력', '2013.04.02', 'A', 248, 1)
    ]
    cur.executemany(insert_sql, books)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_books()