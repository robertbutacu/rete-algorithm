from src.rete.algorithm.Nodes import RootNode
from src.services.mappers.ResponseNode import ResponseNode


def transform_network(node):
    curr_node = ResponseNode()
    if isinstance(node, RootNode):
        curr_node.text.name = "ROOT"
        curr_node.children = map(lambda n: transform_network(node.children[n]), node.children)
        return curr_node
    else:
        curr_node.text.name = node.label
        curr_node.children = map(lambda n: transform_network(node.children[n]), node.children)
        return curr_node


def print_network(network):
    def print_response_node(node, depth):
        print("\t" * depth + " ", node.text.name)
        for n in node.children:
            print_response_node(n, depth + 1)
    for state in network:
        print_response_node(state, 0)




def transform_states(states):
    transformed = []

    for state in states:
        transformed.append(transform_network(state.root_node))

    return transformed


def get_text(file_name):
    # Loads the specified file to be read.
    resource = open(file_name, 'r')

    # Reads the content of the opened file.
    text = resource.read()

    # Closes the opened file.
    resource.close()

    return text
