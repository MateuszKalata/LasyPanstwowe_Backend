def exception_catcher(fun):
    def try_executing(*args, **kwargs):
        try:
            return fun(*args, **kwargs)
        except Exception as ex:
            if isinstance(ex, APIException):
                return {"message": ex.message}, ex.status
            else:
                return {"message": "Unknown exception occured!"}, 500

    try_executing.__name__ = fun.__name__
    return try_executing


class APIException(Exception):
    def __init__(self, message, status=500):
        self.message = message
        self.status = status
        super().__init__(self.message)
