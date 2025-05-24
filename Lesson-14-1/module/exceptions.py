class GroupFullException(Exception):
    def __init__(self, message="Неможливо додати студента: група вже заповнена."):
        super().__init__(message)
