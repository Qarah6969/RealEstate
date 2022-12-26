import user
import database
import submission_base
# because of circular import problem we can't use the 2 following lines.
# from database import DataBase
# from submission_base import SubmissionSell, SubmissionBuy
from typing import Union
from typeguard import typechecked

#available types => 
#خرید = 1
#فروش = -1
#اجاره کردن = 2
#اجاره دادن = -2

@typechecked
class Utility:
    def FindMatch(self, Submission : Union[submission_base.SubmissionSell, submission_base.SubmissionBuy]):
        db = database.DataBase()
        self = Submission

        if isinstance(self, submission_base.SubmissionBuy):
            db.cursor.execute(f"SELECT * FROM sell_submissions WHERE submission_type = {-(self.type)} AND submission_cost >= {self.costA} AND {self.costB} >= submission_cost AND submission_size >= {self.sizeA} AND {self.sizeB} >= submission_rooms AND submission_rooms >= {self.roomsA} AND {self.roomsB} >= submission_rooms AND submission_rent_type = '{self.rent_type}' AND submission_active = 1")
            matches = db.cursor.fetchall()
            db.db.commit()
            if len(matches)>0:
                final_match = list(matches[0])
                submission = submission_base.SubmissionSell(final_match[0], final_match[1], final_match[2], final_match[3], final_match[4], final_match[5], final_match[6], bool(final_match[7]))
                db.add_BuySubmission(self)
                db.set_active(self.id, False, "buy_submissions")
                db.set_active(final_match[0], False, "sell_submissions")
                return submission
            else:
                db.add_BuySubmission(self)
                return []

        if isinstance(self, submission_base.SubmissionSell):
            db.cursor.execute(f"SELECT * FROM buy_submissions WHERE submission_type = {-(self.type)} AND {self.cost} >= submission_costA AND submission_costB >= {self.cost} AND {self.size} >= submission_sizeA AND submission_sizeB >= {self.size} AND {self.rooms} >= submission_roomsA AND submission_roomsB >= {self.rooms} AND submission_rent_type = '{self.rent_type}' AND submission_active = 1")
            matches = db.cursor.fetchall()
            db.db.commit()
            if len(matches)>0:
                final_match = list(matches[0])
                submission = submission_base.SubmissionBuy(final_match[0], final_match[1], final_match[2], final_match[3], final_match[4], final_match[5], final_match[6], final_match[7], final_match[8], final_match[9], bool(final_match[10]))
                db.add_SellSubmission(self)
                db.set_active(self.id, False, "sell_submissions")
                db.set_active(final_match[0], False, "buy_submissions")
                return submission
            else:
                db.add_SellSubmission(self)
                return []
    
    