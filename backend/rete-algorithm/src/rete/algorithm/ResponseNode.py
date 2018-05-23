class ResponseNode():
    def __init__(self, text):
        ResponseNode.__init__(self)

        self.__text = text

        # Dictionary of the children of the node.
        self.__children = []


    @property
    def children(self):
        return self.__children


    @children.setter
    def children(self, value):
        self.__children = value

