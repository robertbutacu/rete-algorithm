from flask import jsonify

from src.rete.algorithm.Nodes import DummyJoinNode, JoinNode, PNode
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
        def build_lower_levels(node):
            result = {}
            if isinstance(node, DummyJoinNode):
                result["text"] = "D.JOIN"
                alpha_memory_dict = {"text": str(node.alpha_memory)}
                alpha_memory_children = []
                for c in node.children:
                    alpha_memory_children.append(build_lower_levels(c))
                    alpha_memory_dict["children"] = alpha_memory_children
                result["children"] = [alpha_memory_dict]

            if isinstance(node, JoinNode):
                result["text"] = "JOIN"
                alpha_memory_dict = {"text": str(node.alpha_memory)}
                alpha_memory_children = []
                for c in node.children:
                    alpha_memory_children.append(build_lower_levels(c))
                    alpha_memory_dict["children"] = alpha_memory_children
                result["children"] = [alpha_memory_dict]

            if isinstance(node, PNode):
                result["text"] = node.name
                result["children"] = []

            return result

        dict_children = []

        for child in self.__children:
            dict_children.append(child.to_dict())

        if self.__alpha_memory_node:
            children = []
            for c in self.__alpha_memory_node.children:
                children.append(build_lower_levels(c))
            dict_children.append({"text": str(self.__alpha_memory_node), "children": children})


        result_dict = {"text": self.__text.to_dict(),
                       "children": dict_children}

        if str(self.__text.name) == "ROOT":
            root_dict = {"activations": self.__activations, "graph": {"chart": {"container": "#tree-simple"},
                                                                      "nodeStructure":
                                                                          result_dict}}
            return root_dict
        else:
            return result_dict
