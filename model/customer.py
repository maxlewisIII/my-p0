class Customer:
    def __init__(self, id, firstname):
        self.id = id
        self.first_name = firstname


    def to_dict(self):
        return {
            "id": self.id,
            "first name": self.first_name,
        }
