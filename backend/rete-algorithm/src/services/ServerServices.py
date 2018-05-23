from src.rete.algorithm.Nodes import RootNode
from src.rete.algorithm.ResponseNode import ResponseNode


def transformNetwork(node):
    currNode = ResponseNode()
    if isinstance(node, RootNode):
        currNode.text.name = "ROOT"
        currNode.children = map(lambda n: transformNetwork(node.children[n]), node.children)
        return currNode
    else:
        currNode.text.name = node.label
        currNode.children = map(lambda n: transformNetwork(node.children[n]), node.children)
        return currNode


def print_response_node(node, depth):
    print("\t" * depth + " ", node.text.name)
    for n in node.children:
        print_response_node(n, depth + 1)