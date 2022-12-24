from typeguard import typechecked

@typechecked
class User:
    def __init__(self, user_id : int, user_username : str, user_password : str, user_type : str):
        self.id = user_id
        self.username = user_username
        self.password = user_password
        self.type = user_type