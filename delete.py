import sqlite3
from select import select_all_books

def delete_books():
    conn = sqlite3.connect("my_books.db")
    cur = conn.execute()

    delete_sql = 'delete from my_books where publisher=?'
    cur.execute(delete_sql, 'A')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    select_all_books()
    delete_books()
    print('[데이터삭제완료]=============================')
    select_all_books()