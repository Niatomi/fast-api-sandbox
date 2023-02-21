class BadRequestException(Exception):
    def __init__(self):
        self.name = "User doesn't exists"