class FileWithStates:
    def __init__(self, text, states):
        self.__text = text
        self.__states = states

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        self.__states = value

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value
