from database import DataBase
from submission_base import SubmissionSell, SubmissionBuy
from typing import Union
from typeguard import typechecked

#available types => 
#خرید = 1
#فروش = -1
#اجاره کردن = 2
#اجاره دادن = -2

@typechecked
class Utility:
    def FindMatch(Submission : Union[SubmissionSell, SubmissionBuy]):
        db = DataBase()
        self = Submission
        if self.type == 1 or self.type == 2:
            db.cursor.execute(f"SELECT * FROM sell_submissions WHERE submission_cost >= {self.costB} AND {self.costA} >= submission_cost AND submission_size >= {self.sizeB} AND {self.sizeA} >= submission_rooms AND submission_rooms >= {self.roomsB} AND {self.roomsA} >= submission_rooms")
            matches = db.cursor.fetchall()
            db.db.commit()
            if len(matches)>0:
                for i in range(len(matches)):
                    matches[i] = list(matches[i])
                final_list = []
                if isinstance(self, SubmissionBuy):
                    for i in matches:
                        submission = SubmissionSell(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                        final_list.append(submission)
                if isinstance(self, SubmissionSell):
                    for i in matches:
                        submission = SubmissionBuy(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10])
                        final_list.append(submission)
                return final_list

        if self.type == -1 or self.type == -2:
            db.cursor.execute(f"SELECT * FROM buy_submissions WHERE submission_costA >= {self.cost} AND {self.cost} >= submission_costB AND submission_sizeA >= {self.size} AND {self.size} >= submission_roomsB AND submission_roomsA >= {self.rooms} AND {self.rooms} >= submission_roomsB")
            matches = db.cursor.fetchall()
            db.db.commit()
            if len(matches)>0:
                for i in range(len(matches)):
                    matches[i] = list(matches[i])
                final_list = []
                if isinstance(self, SubmissionBuy):
                    for i in matches:
                        submission = SubmissionSell(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                        final_list.append(submission)
                if isinstance(self, SubmissionSell):
                    for i in matches:
                        submission = SubmissionBuy(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10])
                        final_list.append(submission)
                return final_list