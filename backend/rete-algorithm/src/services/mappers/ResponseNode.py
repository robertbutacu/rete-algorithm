from src.rete.algorithm.Text import Text


class ResponseNode:
    def __init__(self):
        self.__text = Text("")
        self.__children = []
        self.__alpha_memory_node = ""
        self.__activations = ""

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        self.__children = value

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value

    @property
    def alpha_memory_node(self):
        return self.__alpha_memory_node

    @alpha_memory_node.setter
    def alpha_memory_node(self, value):
        self.__alpha_memory_node = value

    @property
    def activations(self):
        return self.__activations

    @activations.setter
    def activations(self, value):
        self.__activations = value



