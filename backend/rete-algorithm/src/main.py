from src.Builder import Builder
from src.Environment import Environment
from src.Evaluator import Evaluator
from src.functions.FunctionMapper import FunctionMapper
from src.parser.Parser import Parser
from src.rete.algorithm.Network import Network
from src.rete.algorithm.Nodes import RootNode
from src.rete.algorithm.ResponseNode import ResponseNode
from src.rete.algorithm.Strategy import RandomStrategy, BreadthStrategy
from src.services.ServerServices import transformNetwork, print_response_node

if __name__ == "__main__":
    parser = Parser()
    builder = Builder()
    functionMapper = FunctionMapper()
    environment = Environment()
    evaluator = Evaluator(environment, functionMapper)
    strategy = BreadthStrategy()
    network = Network(evaluator, strategy)

    parsedFile = parser.parseFile("E:\\Projects\\rete-algorithm\\backend\\rete-algorithm\\src\\examples\\general-truths.clp")

    (facts, rules) = builder.build(parsedFile)
    print("Building network")
    result = network.build_network(facts, rules)

    print("Network built - working on transforming it!")
    for x in result:
        transformed = transformNetwork(x.root_node)
        print_response_node(transformed, 0)
        print("\n\n\n")
