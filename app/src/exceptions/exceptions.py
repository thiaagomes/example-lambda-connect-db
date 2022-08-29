class BusinessException(Exception):
    def __init__(self, message) -> None:
        self.status_code = 400
        self.message = message
        super().__init__({
            'status_code': 400,
            'message': message
        })