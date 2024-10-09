from db.servise import DB


class Customer(DB):
    def __init__(self, *param,
                 id: int = None,
                 first_name: str = None,
                 last_name: str = None,
                 username: str = None,
                 phone_number: str = None,
                 created_at: str = None, ):
        self.param = param
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone_number = phone_number
        self.created_at = created_at
