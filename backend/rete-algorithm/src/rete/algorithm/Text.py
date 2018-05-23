class Text():
    def __init__(self, text):
        Text.__init__(self)

        self.__text = text

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value
