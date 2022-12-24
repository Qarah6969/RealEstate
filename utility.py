import user
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
                final_match = matches[0]
                if isinstance(self, SubmissionBuy):
                    submission = SubmissionSell(final_match[0], final_match[1], final_match[2], final_match[3], final_match[4], final_match[5], final_match[6], final_match[7])
                if isinstance(self, SubmissionSell):
                    submission = SubmissionBuy(final_match[0], final_match[1], final_match[2], final_match[3], final_match[4], final_match[5], final_match[6], final_match[7], final_match[8], final_match[9], final_match[10])
                db.add_BuySubmission(self)
                db.set_active(self.id, False, "buy_submissions")
                return submission
            else:
                db.add_BuySubmission(self)
                return []

        if self.type == -1 or self.type == -2:
            db.cursor.execute(f"SELECT * FROM buy_submissions WHERE submission_costA >= {self.cost} AND {self.cost} >= submission_costB AND submission_sizeA >= {self.size} AND {self.size} >= submission_roomsB AND submission_roomsA >= {self.rooms} AND {self.rooms} >= submission_roomsB")
            matches = db.cursor.fetchall()
            db.db.commit()
            if len(matches)>0:
                final_match = matches[0]
                if isinstance(self, SubmissionBuy):
                    submission = SubmissionSell(final_match[0], final_match[1], final_match[2], final_match[3], final_match[4], final_match[5], final_match[6], final_match[7])
                if isinstance(self, SubmissionSell):
                    submission = SubmissionBuy(final_match[0], final_match[1], final_match[2], final_match[3], final_match[4], final_match[5], final_match[6], final_match[7], final_match[8], final_match[9], final_match[10])
                db.add_SellSubmission(self)
                db.set_active(self.id, False, "sell_submissions")
                return submission
            else:
                db.add_SellSubmission(self)
                return []
    
    
