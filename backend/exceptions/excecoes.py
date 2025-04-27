class CpfAlreadyExist(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)



class CpfInvalid(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)



class PasswordDoNotMatch(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class EmailInvalid(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)