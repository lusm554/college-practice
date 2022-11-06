import sqlite3
import os

class DB:
    def __init__(self, db_name: str = "university.db", newone_db: bool = True,
                 sample_name: str = "sample_data.sql") -> None:
        try:
            self.db_name = db_name
            self.sample_script = sample_name
        
            # Clear database
            if newone_db:
                self.__clear_db__()
        
            # Connect to database
            self.con = sqlite3.connect(db_name)
            self.cur = self.con.cursor()

            # Create sample data
            self.__create_sample__()
        except Exception as e:
            raise e
            print(f"Error: {e}")

    def __create_sample__(self):
        with open(self.sample_script, 'r') as sql_file:
            sql_script = sql_file.read() 
            self.cur.executescript(sql_script)
            self.con.commit()

    def __clear_db__(self):
        try:
            os.remove(self.db_name)
        except FileNotFoundError:
            print(f"Data base '{self.db_name}' not found. Creating new one.")


if __name__ == "__main__":
    # Connect, set tables, insert sample data
    db = DB()

    tables = ['students', 'teachers', 'groups', 'dissertations', 'Faculty',
     'Departments', 'Disciplines', 'disciplines_schedule', 'Session',
     'Graduate_works']

    for t in tables:
        print(t)
        res = db.cur.execute(f"select * from {t}")
        print(res.fetchall())
        print()



