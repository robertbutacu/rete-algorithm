from src.Builder import Builder
from src.Environment import Environment
from src.Evaluator import Evaluator
from src.functions.FunctionMapper import FunctionMapper
from src.parser.Parser import Parser
from src.rete.algorithm.Network import Network
from src.rete.algorithm.Strategy import RandomStrategy, BreadthStrategy

if __name__ == "__main__":
    def printNode(node):
        t = 0
        for key in node.children:
            print(t * "\t" + str(key))
            print(t * "\t" + str(node.children[key].label))
            t += 1

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
        printNode(x.root_node)
