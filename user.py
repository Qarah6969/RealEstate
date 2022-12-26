import database
import submission_base
import utility
from typeguard import typechecked
from typing import Union
# because of circular import problem we can't use the 3 following lines.
# from database import DataBase
# from submission_base import SubmissionBuy, SubmissionSell
# from utility import FindMatch

@typechecked
class User:
    def __init__(self, user_id : int, user_username : str, user_password : str, user_type : int):
        self.id = user_id
        self.username = user_username
        self.password = user_password
        self.type = user_type

#available types => 
#0 = guest
#1 = user
#3 = operator

    @typechecked
    def SignUp(self, username : str, password : str):
        db = database.DataBase()
        db.cursor.execute("SELECT user_id FROM users")
        if len(db.cursor.fetchall()) == 0:
            id = 1
        else:
            db.cursor.execute("SELECT user_id FROM users")
            id = int(db.cursor.fetchall().pop()[0]) + 1
        db.db.commit()
        CurrentUser = User(id, username, password, 1)
        db.add_user(CurrentUser)    
        return CurrentUser

    @typechecked
    def SignIn(self, username : str, password : str):
        db = database.DataBase()
        db.cursor.execute(f"SELECT * FROM users WHERE user_username = '{username}' AND user_password = '{password}'")
        usratrs = db.cursor.fetchall()
        db.db.commit()
        CurrentUser = User(usratrs[0][0], usratrs[0][1], usratrs[0][2], usratrs[0][3])
        return CurrentUser

    def SignOut(self):
        CurrentUser = User(0, "guest", "", 0)
        return CurrentUser

    @typechecked
    def SubmitBuy(self, submission_type : int, submission_costA: int, submission_costB: int, submission_sizeA : int, submission_sizeB : int, submission_roomsA : int, submission_roomsB : int, submission_rent_type : Union[str, None]):
        if self.type == 1: #Added
            db = database.DataBase()
            db.cursor.execute(f"SELECT submission_id FROM buy_submissions")
            if len(db.cursor.fetchall()) == 0:
                id = 1
            else:
                db.cursor.execute("SELECT submission_id FROM buy_submissions")
                id = int(db.cursor.fetchall().pop()[0]) + 1
            db.db.commit()
            submission = submission_base.SubmissionBuy(id, submission_type, submission_costA, submission_costB, submission_sizeA, submission_sizeB, submission_roomsA, submission_roomsB, self.username, submission_rent_type, True)
            return utility.Utility().FindMatch(submission)
        else:
            return False #Added
    
    @typechecked
    def SubmitSell(self, submission_type : int, submission_cost: int, submission_size : int, submission_rooms : int, submission_rent_type : Union[str, None]):
        if self.type == 1: #Added
            db = database.DataBase()
            db.cursor.execute(f"SELECT submission_id FROM sell_submissions")
            if len(db.cursor.fetchall()) == 0:
                id = 1
            else:
                db.cursor.execute("SELECT submission_id FROM sell_submissions")
                id = int(db.cursor.fetchall().pop()[0]) + 1
            db.db.commit()
            submission = submission_base.SubmissionSell(id, submission_type, submission_cost, submission_size, submission_rooms, self.username, submission_rent_type, True)
            return utility.Utility().FindMatch(submission)
        else:
            return False  #Added

    #Added
    @typechecked
    def AddAdmin(self, username : str, password : str):
        db = database.DataBase()
        if self.type == 3:
            db.cursor.execute("SELECT user_id FROM users")
            id = int(db.cursor.fetchall().pop()[0]) + 1
            db.db.commit()
            db.add_user(User(id, username, password, 3))