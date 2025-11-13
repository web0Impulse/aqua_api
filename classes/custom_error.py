class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.data = {'message': message }