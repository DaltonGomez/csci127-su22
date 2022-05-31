class MyProtectedClass:

    def __init__(self):
        self.publicData = "For Any Eyes"
        self._protectedData = "For Friends Eyes Only"


class MyPrivateClass:

    def __init__(self):
        self.publicData = "For Any Eyes"
        self.__privateData = "For These Eyes Only"
