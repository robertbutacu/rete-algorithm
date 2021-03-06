from src.Builder import Builder
from src.Environment import Environment
from src.functions.FunctionMapper import FunctionMapper
from src.parser.Parser import Parser
from src.rete.algorithm.Network import Network
from src.rete.algorithm.Strategy import BreadthStrategy
from src.services.TransformerServices import transform_states, get_text
from src.services.mappers.FileWithStates import FileWithStates


def build_network(text, is_with_file):
    parser = Parser()
    builder = Builder()
    function_mapper = FunctionMapper()
    environment = Environment()
    strategy = BreadthStrategy()

    if is_with_file:
        parsed_file = parser.parse_file(text)

        (facts, rules) = builder.build(parsed_file)
        evaluator = builder.evaluator
        network = Network(evaluator, strategy)

        print("Building network from file")
        result = network.build_network(facts, rules)

        print("Network built - working on transforming it!")
        transformed = transform_states(result)

        print("Transformed - > returning result")
        return FileWithStates(get_text(text), transformed)
    else:
        parsed_text = parser.parseProgram(text)
        (facts, rules) = builder.build(parsed_text)
        evaluator = builder.evaluator
        network = Network(evaluator, strategy)

        print("Building network from text")

        result = network.build_network(facts, rules)

        print("Network built - working on transforming it!")
        transformed = transform_states(result)

        print("Transformed -> returning result")

        return transformed


def get_example_service(example_name):
    examples = {"1": "..\\examples\\Social.clp",
                "2": "..\\examples\\general-truths.clp",
                "3": "..\\examples\\sillogismi.clp",
                "4": "..\\examples\\Social.clp"}

    return build_network(examples[example_name], True)