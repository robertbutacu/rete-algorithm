from flask import jsonify

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

    def to_dict(self):
        dict_children = []

        for child in self.__children:
            dict_children.append(child.to_dict())

        if self.__alpha_memory_node is not None:
            dict_children.append({"text": str(self.__alpha_memory_node), "children": []})

        result_dict = {"text": self.__text.to_dict(),
                       "children": dict_children}

        if str(self.__text.name ) == "ROOT":
            root_dict = {}
            root_dict["activations"] = self.__activations
            root_dict["graph"] = result_dict
            return root_dict
        else:
            return result_dict
