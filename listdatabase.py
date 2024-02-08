import sqlite3
connect=sqlite3.connect(r'E:\PYTHON\PROJECTS\TO-DO LIST\Tasks_List.db')
c=connect.cursor()
c.execute('''CREATE TABLE Task_List(
          Task text,
          Date_added text,
          CompletedTask text
          
)''')
connect.commit()
connect.close()