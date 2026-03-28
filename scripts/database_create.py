import sqlite3

conn = sqlite3.connect('datos/salud.db')

c=conn.cursor()

c.execute("""CREATE TABLE CCDR(
          
          year int,
          enfermedad text,
          Grupo text,
          SubGrupo text,
          Estado text,
          Muertos int
        )""")

conn.commit()
conn.close()