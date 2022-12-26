import sqlite3 as sql
import submission_base
import user
# because of circular import problem we can't use the 2 following lines.
# from submission_base import SubmissionSell, SubmissionBuy
# from user import User
from typeguard import typechecked
from typing import Union
from config import Config

@typechecked
class DataBase:
    def __init__(self):
        self.db : sql.Connection = sql.connect(Config.database_path)
        self.cursor : sql.Cursor = self.db.cursor() 
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users 
                (user_id INT UNIQUE,
                user_username TEXT UNIQUE,
                user_password TEXT,
                user_type INT)
            """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS sell_submissions 
                (submission_id INT UNIQUE,
                submission_type INT,
                submission_cost INT,
                submission_size INT,
                submission_rooms INT,
                submission_applicant TEXT,
                submission_rent_type TEXT,
                submission_active INT)
            """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS buy_submissions 
                (submission_id INT UNIQUE,
                submission_type INT,
                submission_costA INT,
                submission_costB INT,
                submission_sizeA INT,
                submission_sizeB INT,
                submission_roomsA INT,
                submission_roomsB INT,
                submission_applicant TEXT,
                submission_rent_type TEXT,
                submission_active INT)
            """)
        self.cursor.execute("INSERT OR IGNORE INTO users VALUES(1, 'admin', 'admin', 3)")
        self.db.commit()
    
    @typechecked
    def add_SellSubmission(self, submission : submission_base.SubmissionSell):
        self.cursor.execute("INSERT INTO sell_submissions VALUES (?,?,?,?,?,?,?,?)", (submission.id, submission.type, submission.cost, submission.size, submission.rooms, submission.applicant, submission.rent_type, submission.active))
        self.db.commit()

    @typechecked
    def add_BuySubmission(self, submission : submission_base.SubmissionBuy):
        self.cursor.execute("INSERT INTO buy_submissions VALUES (?,?,?,?,?,?,?,?,?,?,?)", (submission.id, submission.type, submission.costA, submission.costB, submission.sizeA, submission.sizeB, submission.roomsA, submission.roomsB, submission.applicant, submission.rent_type, submission.active))
        self.db.commit()

    @typechecked   
    def add_user(self, user : user.User):
        self.cursor.execute("INSERT INTO users VALUES (?,?,?,?)", (user.id, user.username, user.password, user.type))
        self.db.commit()

    @typechecked
    def get_items(self, table : str):
        options = ["users", "sell_submissions", "buy_submissions"]
        if table not in options: 
            raise AttributeError("Inavlid Table Name")
        self.cursor.execute(f"SELECT * FROM {table}")
        items = self.cursor.fetchall()
        for i in range(len(items)):
            items[i] = list(items[i])
        final_list = []
        if table == "users":
            for i in items:
                user = User(i[0], i[1], i[2], i[3])
                final_list.append(user)
        if table == "sell_submissions":
            for i in items:
                submission = SubmissionSell(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                final_list.append(submission)
        if table == "buy_submissions":
            for i in items:
                submission = SubmissionBuy(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10])
                final_list.append(submission)
        return final_list

    @typechecked
    def get_applicant_submissions(self, applicant : str):
        self.cursor.execute(f"SELECT * FROM sell_submissions WHERE submission_applicant = '{applicant}'")
        sells = self.cursor.fetchall()
        self.db.commit()
        self.cursor.execute(f"SELECT * FROM buy_submissions WHERE submission_applicant = '{applicant}'")
        buys = self.cursor.fetchall()
        self.db.commit()
        return sells, buys

    @typechecked
    def set_active(self, id : int, active : bool, table : str):
        active = 1 if active else 0
        self.cursor.execute(f"""UPDATE {table} SET submission_active = {active}
                WHERE submission_id = {id}
                """)
        self.db.commit()

    @typechecked
    def validate_user(self, username : str, password : Union[str, None]):  
        username_stat = False
        self.cursor.execute("SELECT user_username FROM users")
        items = self.cursor.fetchall()
        for i in range(len(items)):
            items[i] = items[i][0]
        self.db.commit()
        if username in items: 
            username_stat = True
        if not password:
            return username_stat
        if not username_stat:
            return False
        self.cursor.execute("SELECT user_password FROM users")
        items = self.cursor.fetchall()
        for i in range(len(items)):
            items[i] = items[i][0]
        self.db.commit()
        if password in items:
            return True
        else:
            return False