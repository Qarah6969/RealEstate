from typeguard import typechecked
from typing import Union

@typechecked
class SubmissionSell:
    def __init__(self, submission_id : int, submission_type : int, submission_cost: int, submission_size : int, submission_rooms : int, submission_apllicant : str, submission_rent_type : Union[str, None], submission_active : bool = True):
        self.id = submission_id
        self.type = submission_type
        #available types => 
        #خرید = 1
        #فروش = -1
        #اجاره کردن = 2
        #اجاره دادن = -2
        self.cost = submission_cost
        self.size = submission_size
        self.rooms = submission_rooms
        self.applicant = submission_apllicant
        self.rent_type = submission_rent_type or "NULL"
        self.active = submission_active 

@typechecked
class SubmissionBuy:
    def __init__(self, submission_id : int, submission_type : int, submission_costA: int, submission_costB: int, submission_sizeA : int, submission_sizeB : int, submission_roomsA : int, submission_roomsB : int, submission_apllicant : str, submission_rent_type : Union[str, None], submission_active : bool = True):
        self.id = submission_id
        self.type = submission_type
        #available types => 
        #خرید = 1
        #فروش = -1
        #اجاره کردن = 2
        #اجاره دادن = -2
        self.costA = submission_costA
        self.costB = submission_costB
        self.sizeA = submission_sizeA
        self.sizeB = submission_sizeB
        self.roomsA = submission_roomsA
        self.roomsB = submission_roomsB
        self.applicant = submission_apllicant
        self.rent_type = submission_rent_type or "NULL"
        self.active = submission_active 