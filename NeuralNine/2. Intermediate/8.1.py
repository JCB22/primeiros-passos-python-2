"""

Inicia este programa somente quando o arquivo que ele referencia já
tiver uma tabela inicializada e algumas informações inseridas

"""
import sqlite3

class Person:

    def __init__(self, id_number=1, first='', last="", age=-1):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect('mydata')
        self.cursor = self.connection.cursor()

    def load_person(self, id_number):
        self.cursor.execute(f"""
        SELECT * FROM persons
        WHERE id = {id_number}
        """)

        results = self.cursor.fetchone()

        self.id_number = id_number
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]

    def insert_person(self):
        self.cursor.execute(
            F"""
            INSERT INTO persons VALUES 
            ({self.id_number}, {self.first}, {self.last}, {self.age})
            """
        )

        self.connection.commit()


p1 = Person(7, "Alex", "Robbins", 30)

#p1.load_person(7)
#print(p1.first)
#print(p1.last)
#print(p1.age)

connection = sqlite3.connect("mydata")
cursor = connection.cursor()

cursor.execute(f'''SELECT * FROM persons''')
results = cursor.fetchall()
print(results)