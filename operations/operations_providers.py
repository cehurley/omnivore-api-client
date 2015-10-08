

class OperationsProvider(object):
    def __init__(self, opCallBack):
        self.op_call_back = opCallBack
        self.operation = None

    def __getattr__(self, attr):
        self.operation = attr
        return self

    def __call__(self, **kwargs):
        return self.op_call_back(self.operation, kwargs)
