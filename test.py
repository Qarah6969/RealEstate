from database import DataBase
from utility import Utility
from submission_base import SubmissionSell, SubmissionBuy

#available types => 
#خرید = 1
#فروش = -1
#اجاره کردن = 2
#اجاره دادن = -2

db = DataBase()
#sb0 = SubmissionSell(".", ".", ".", ".", ".", ".", ".")
sb = SubmissionSell(1, -1, 950, 8, 5, "bababoy","mahane")
sb2 = SubmissionSell(2, -1, 500, 1, 0, "bababoy","mahane")
sb3 = SubmissionBuy(1, 1, 700, 450, 2, 0, 1, 0, "Nigger", None, True)
sb4 = SubmissionBuy(0, 1, 1000, 900, 10, 5, 7, 3, "Nigger", None, True)
sb5 = SubmissionBuy(0, 1, 1000, 400, 10, 1, 7, 0, "Nigger", None, True)
db.add_SellSubmission()
db.add_BuySubmission()
print(db.get_items("sell_submissions"))
print(db.get_items("buy_submissions"))
print("BEFORE SLEEP")
print("AFTER SLEEP")
print(Utility.FindMatch())
