import sqlite3
from select import select_one_book

def update_books():
    conn = sqlite3.connect("my_books.db")
    cur = conn.cursor()

    update_sql = 'update my_books set recommendation=recommendation+? where title =?'

    cur.execute(update_sql, (1, '개발자의 코드'))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    select_one_book()
    update_books()
    print('[데이터 수정 완료]=================================')
    select_one_book()