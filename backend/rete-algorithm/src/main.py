from src.Builder import Builder
from src.Environment import Environment
from src.Evaluator import Evaluator
from src.functions.FunctionMapper import FunctionMapper
from src.parser.Parser import Parser
from src.rete.algorithm.Network import Network
from src.rete.algorithm.Nodes import RootNode
from src.rete.algorithm.ResponseNode import ResponseNode
from src.rete.algorithm.Strategy import RandomStrategy, BreadthStrategy

if __name__ == "__main__":
    def transformNetwork(node):
        currNode = ResponseNode()
        if isinstance(node, RootNode):
            currNode.text.name = "ROOT"
            currNode.children = map(lambda n: transformNetwork(n), node.children)
            return currNode
        elif isinstance(node, None):
            return None
        else:
            print(type(node))
            currNode.text.name = node.label
            currNode.children = map(lambda n: transformNetwork(n), node.children)
            return currNode

    parser = Parser()
    builder = Builder()
    functionMapper = FunctionMapper()
    environment = Environment()
    evaluator = Evaluator(environment, functionMapper)
    strategy = BreadthStrategy()
    network = Network(evaluator, strategy)

    parsedFile = parser.parseFile("E:\\Projects\\turtle\\docs\\examples\\Blocchi.clp")

    (facts, rules) = builder.build(parsedFile)
    print("building network")
    result = network.build_network(facts, rules)
    for x in result:
        print(transformNetwork(x.root_node))
