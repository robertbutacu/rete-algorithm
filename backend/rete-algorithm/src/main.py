from src.Builder import Builder
from src.Environment import Environment
from src.Evaluator import Evaluator
from src.functions.FunctionMapper import FunctionMapper
from src.parser.Parser import Parser
from src.rete.algorithm.Network import Network
from src.rete.algorithm.Strategy import RandomStrategy, BreadthStrategy

if __name__ == "__main__":
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
        print(x.root_node.network)
