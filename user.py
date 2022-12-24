from typeguard import typechecked
from database import DataBase
from submission_base import SubmissionBuy, SubmissionSell
from utility import FindMatch

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
        db = DataBase()
        if validate_user(username):
            db.cursor.execute("SELECT rowid FROM users")
            id = db.cursor.fetchall()[-1] + 1
            db.db.commit()
            CurrentUser = User(id, username, password, 1)
            db.add_user(CurrentUser)    
            return CurrentUser

    @typechecked
    def SignIn(self, username : str, password : str):
        db = DataBase()
        if validate_user(username, password):
            db.cursor.execute(f"SELECT * FROM users WHERE username = {username} AND password = {password}")
            usratrs = db.cursor.fetchall()
            db.db.commit()
            CurrentUser = User(usratrs[0], usratrs[1], usratrs[2], usratrs[3])
            return CurrentUser

    def SignOut(self):
        CurrentUser = User(0, "guest", "", 0)
        return CurrentUser

    @typechecked
    def SubmitBuy(self, submission_type : int, submission_costA: int, submission_costB: int, submission_sizeA : int, submission_sizeB : int, submission_roomsA : int, submission_roomsB : int, submission_rent_type : Union[str, None]):
        db = DataBase()
        db.cursor.execute(f"SELECT submission_id FROM buy_submissions")
        id = db.cursor.fetchall()[-1] + 1
        db.db.commit()
        submission = SubmissionBuy(id, submission_type, submission_costA, submission_costB, submission_sizeA, submission_sizeB, submission_roomsA, submission_roomsB, self.username, submission_rent_type, True)
        return FindMatch(submission)
    
    @typechecked
    def SubmitSell(self, submission_type : int, submission_cost: int, submission_size : int, submission_rooms : int, , submission_rent_type : Union[str, None])
        db = DataBase()
        db.cursor.execute(f"SELECT submission_id FROM sell_submissions")
        id = db.cursor.fetchall()[-1] + 1
        db.db.commit()
        submission = SubmissionSell(id, submission_type, submission_cost, submission_size, submission_rooms, self.username, submission_rent_type, True)
        return FindMatch(submission)
