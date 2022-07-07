class Customer:
    def __init__(self, id, first_name):
        self.id = id
        self.first_name = first_name


    def to_dict(self):
        return {
            "id": self.id,
            "first name": self.first_name
        }
