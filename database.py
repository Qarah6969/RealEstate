import sqlite3 as sql
from submission_base import SubmissionSell, SubmissionBuy
from user import User
from typeguard import typechecked
from config import Config

@typechecked
class DataBase:
    def __init__(self):
        self.db : sql.Connection = sql.connect(Config.database_path)
        self.cursor : sql.Cursor = self.db.cursor() 
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users 
                (user_id INT,
                user_username TEXT,
                user_password TEXT,
                user_type TEXT)
            """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS sell_submissions 
                (submission_id INT,
                submission_type INT,
                submission_cost INT,
                submission_size INT,
                submission_rooms INT,
                submission_applicant TEXT,
                submission_rent_type TEXT,
                submission_active INT)
            """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS buy_submissions 
                (submission_id INT,
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
        self.db.commit()
    
    @typechecked
    def add_SellSubmission(self, submission : SubmissionSell):
        self.cursor.execute("INSERT INTO sell_submissions VALUES (?,?,?,?,?,?,?,?)", (submission.id, submission.type, submission.cost, submission.size, submission.rooms, submission.applicant, submission.rent_type, submission.active))
        self.db.commit()

    @typechecked
    def add_BuySubmission(self, submission : SubmissionBuy):
        self.cursor.execute("INSERT INTO buy_submissions VALUES (?,?,?,?,?,?,?,?,?,?,?)", (submission.id, submission.type, submission.costA, submission.costB, submission.sizeA, submission.sizeB, submission.roomsA, submission.roomsB, submission.applicant, submission.rent_type, submission.active))
        self.db.commit()

    @typechecked   
    def add_user(self, user : User):
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
    def set_active(self, id : int, active : bool, table : str):
        active = 1 if active else 0
        self.cursor.execute(f"""UPDATE {table} SET active = {active}
                WHERE submission_id = {id}
                """)
        self.db.commit()

    @typechecked
    def check_username_exists(self, username : str):
        self.cursor.execute("SELECT username FROM users")
        items = self.cursor.fetchall()
        for i in range(len(items)):
            items[i] = list(items[i])
        self.db.commit()
        if username in items:
            return False
        else:
            return True
    
    @typechecked
    def check_password_exists(self, password : str):
        self.cursor.execute("SELECT password FROM users")
        items = self.cursor.fetchall()
        for i in range(len(items)):
            items[i] = list(items[i])
        self.db.commit()
        if password in items:
            return False
        else:
            return True
