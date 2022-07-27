"""

Pego do comentário do vídeo do Youtube:
I think the best option to use database is using within context manager. It solves a lot of
issues like closing connection:

def count_table():
    with sqlite3.connect(DB_NAME) as db:
        num_of_rows = db.execute(SQL_COUNT).fetchall()
    return num_of_rows[0]


"""


import sqlite3


if __name__ == "__main__":

    connection = sqlite3.connect('mydata')

    cursor = connection.cursor()

    cursor.execute("""
     CREATE TABLE IF NOT EXISTS persons (
         id INTEGER PRIMARY KEY,
        first_name varchar(32),
         last_name varchar(32),
         age int
     )
     """)


    cursor.execute("""
         INSERT INTO persons VALUES
         (1, 'Paul', 'Smith', 32),
         (2, 'Mark', 'Johnson', 24),
         (3, 'Anna', 'Smith', 34)
     """)

    connection.commit()

    connection.close()
