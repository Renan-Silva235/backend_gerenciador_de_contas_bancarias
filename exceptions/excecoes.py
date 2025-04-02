class CpfAlreadyExist(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)



class CpfInvalid(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)