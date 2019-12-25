import sqlite3

def select_all_books():
    conn = sqlite3.connect("my_books.db")
    cur = conn.cursor()
    cur.execute('select * from my_books')

    print('[1] 전체 데이터 출력하기')
    books = cur.fetchall()

    for book in books:
        print (book)

    conn.close()

def select_some_books(number):
    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    cur.execute('select * from my_books')
    print('[2] 데이터 일부 출력하기')
    books = cur.fetchmany(number)

    for book in books:
        print(book)

    conn.close();

def select_one_book():
    conn = sqlite3.connect("my_books.db")
    cur = conn.cursor()

    cur.execute("select * from my_books")

    book = cur.fetchone()
    print("[3] 데이터 1건 출력하기")
    print(book)

    conn.close()


def find_big_books():
    conn = sqlite3.connect("my_books.db")
    cur = conn.cursor()

    cur.execute('select title, pages from my_books where pages > 300')
    print('[4] 페이지 많은책 출력하기')
    books = cur.fetchall()
    for book in books:
        print(book)

    conn.close()

if __name__ == "__main__":
    select_all_books()
    select_some_books(2)
    select_one_book()
    find_big_books()
