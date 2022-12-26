import os
from database import DataBase
from submission_base import SubmissionBuy, SubmissionSell
from user import User

os.system('cls')
db = DataBase()
CurrentUser = User(0, "guest", "", 0) #Sets the current user as guest
print("Welcome.")
while True:
    if CurrentUser.type == 0:
        print("Press 1 if you want to Signup.\nPress 2 if you want to SignIn.\nPress 3 to quit.")
        key : int = int(input())
        if key == 1:
            while True:
                os.system('cls')
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                if not db.validate_user(username, None):
                    CurrentUser = CurrentUser.SignUp(username, password)
                    print("Signed up successfully.")
                    break
                else:
                    os.system('cls')
                    print("Username exists.")
                    if input("Continue? ").lower() == "yes":
                        continue
                    else:
                        break
        elif key == 2:
            while True:
                os.system('cls')
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                if db.validate_user(username, password):
                    CurrentUser = CurrentUser.SignIn(username, password)
                    break
                else:
                    os.system('cls')
                    print("Your username or password is incorrect.")
                    if input("Continue? ").lower() == "yes":
                        continue
                    else:
                        break
        elif key == 3:
            os.system('cls')
            exit()
    
    if CurrentUser.type != 0:
        os.system('cls')
        print(f"Welcome {CurrentUser.username}")
        while True:
            if CurrentUser.type == 1:
                print("Press 1 to submit a selling request.\nPress 2 to submit a buying request.\nPress 3 to see your submissions.\nPress 4 to logout.\nPress 5 to quit.")
                key : int = int(input())
                if key == 1:
                    os.system('cls')
                    if input("Sale or Rent : ").lower() == "sale":
                        selling_type = -1 
                    else :
                        selling_type = -2
                    if selling_type == -2:
                        rent_type = input("Monthly or Mortgage : ").lower()
                    else: 
                        rent_type = None
                    cost = int(input("Cost : "))
                    size = int(input("Size : "))
                    rooms = int(input("Rooms : "))
                    match = CurrentUser.SubmitSell(selling_type, cost, size, rooms, rent_type)
                    if match == []:
                        input("Your request has been added to database. Press any key and enter to continue.")
                    else:
                        print("Here is matching request for you: ")
                        if rent_type == None:
                            print(f"id : {match.id}\tbuying type : {match.type}\tmin and max cost(in Toman) : {match.costA},{match.costB}\tmin and max size(in square meters) : {match.sizeA},{match.sizeB}\tmin and max rooms : {match.roomsA},{match.roomsB}")
                        else:
                            print(f"id : {match.id}\tbuying type : {match.type}\tmin and max cost(in Toman) : {match.costA},{match.costB}\tmin and max size(in square meters) : {match.sizeA},{match.sizeB}\tmin and max rooms : {match.roomsA},{match.roomsB}\t\trent type : {match.rent_type}")
                    os.system('cls')
                elif key == 2:
                    os.system('cls')
                    if input("Buy or Rent : ").lower() == "buy":
                        buying_type = 1 
                    else :
                        buying_type = 2
                    if buying_type == 2:
                        rent_type = input("Monthly or Mortgage : ").lower()
                    else: 
                        rent_type = None
                    mincost = int(input("Min Cost : "))
                    maxcost = int(input("Max Cost : "))
                    minsize = int(input("Min Size : "))
                    maxsize = int(input("Max Size : "))
                    minrooms = int(input("Min Rooms : "))
                    maxrooms = int(input("Max Rooms : "))
                    match = CurrentUser.SubmitBuy(buying_type, mincost, maxcost, minsize, maxsize, minrooms, maxrooms, rent_type)
                    if match == []:
                        input("Your request has been added to database. Press any key and enter to continue.")
                    else:
                        print("Here is matching request for you: ")
                        if rent_type == None:
                            print(f"id : {match.id}\tselling type : {match.type}\tcost(in Toman) : {match.cost}\tsize(in square meters) : {match.size}\trooms : {match.rooms}")
                        else:
                            print(f"id : {match.id}\tselling type : {match.type}\tcost(in Toman) : {match.cost}\tsize(in square meters) : {match.size}\trooms : {match.rooms}\trent type : {match.rent_type}")
                    os.system('cls')
                elif key == 3:
                    os.system('cls')
                    sells, buys = db.get_applicant_submissions(CurrentUser.username)
                    if sells != []:
                        print("Your selling requests: ")
                        for i in sells:
                            i = list(i)
                            if i[1] == -1 : i[1] = "sale"
                            elif i[1] == -2 : i[1] = "rent"
                            if i[7] == 1 : i[7] = True
                            else : i[7] = False
                            if i[6] == "NULL":
                                print(f"id : {i[0]}\tselling type : {i[1]}\tcost(in Toman) : {i[2]}\tsize(in square meters) : {i[3]}\trooms : {i[4]}\tactive : {i[7]}")
                            else:
                                print(f"id : {i[0]}\tselling type : {i[1]}\tcost(in Toman) : {i[2]}\tsize(in square meters) : {i[3]}\trooms : {i[4]}\trent type : {i[6]}\tactive : {i[7]}")
                    else:
                        print("You don't have any selling requests.")
                    if buys != []:
                        print("-------------------\nYour buying requests: ")
                        for i in buys:
                            i = list(i)
                            if i[1] == 1 : i[1] = "buy"
                            elif i[1] == 2 : i[1] = "rent"
                            if i[10] == 1 : i[10] = True
                            else : i[10] = False
                            if i[9] == "NULL":
                                print(f"id : {i[0]}\tbuying type : {i[1]}\tmin and max cost(in Toman) : {i[2]},{i[3]}\tmin and max size(in square meters) : {i[4]},{i[5]}\tmin and max rooms : {i[6]},{i[7]}\t\tactive : {i[10]}")
                            else:
                                print(f"id : {i[0]}\tbuying type : {i[1]}\tmin and max cost(in Toman) : {i[2]},{i[3]}\tmin and max size(in square meters) : {i[4]},{i[5]}\tmin and max rooms : {i[6]},{i[7]}\t\trent type : {i[9]}\tactive : {i[10]}")
                    else:
                        print("You don't have any buying requests.")
                    input("press any key or enter to get back to menu")
                    os.system('cls')
                elif key == 4:
                    CurrentUser = User(0, "guest", "", 0)
                    os.system('cls')
                    break
                elif key == 5:
                    os.system('cls')
                    exit()
                