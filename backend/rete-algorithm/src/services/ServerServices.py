from src.Builder import Builder
from src.Environment import Environment
from src.Evaluator import Evaluator
from src.functions.FunctionMapper import FunctionMapper
from src.parser.Parser import Parser
from src.rete.algorithm.Network import Network
from src.rete.algorithm.Strategy import BreadthStrategy
from src.services.TransformerServices import transform_states, print_response_node
from src.services.mappers.FileWithStates import FileWithStates


def build_network(text, is_with_file):
    def get_text(file_name):
        # Loads the specified file to be read.
        resource = open(file_name, 'r')

        # Reads the content of the opened file.
        text = resource.read()

        # Closes the opened file.
        resource.close()

        return text

    parser = Parser()
    builder = Builder()
    function_mapper = FunctionMapper()
    environment = Environment()
    evaluator = Evaluator(environment, function_mapper)
    strategy = BreadthStrategy()
    network = Network(evaluator, strategy)

    if is_with_file:
        parsed_file = parser.parseFile(text)

        (facts, rules) = builder.build(parsed_file)
        print("Building network")
        result = network.build_network(facts, rules)

        print("Network built - working on transforming it!")

        return FileWithStates(get_text(text), transform_states(result))
    else:
        parsed_text = parser.parseProgram(text)
        (facts, rules) = builder.build(parsed_text)

        print("Building network")
        result = network.build_network(facts, rules)

        print("Network built - working on transforming it!")
        return transform_states(result)




