"E:\\Projects\\rete-algorithm\\backend\\rete-algorithm\\src\\examples\\Social.clp"
from src.services.ServerServices import build_network
from src.services.TransformerServices import get_text, print_network

if __name__ == "__main__":
    network = build_network(
        get_text("E:\\Projects\\rete-algorithm\\backend\\rete-algorithm\\src\\examples\\Social.clp"),
        False)
    print_network(network)

    #file_response = build_network("E:\\Projects\\rete-algorithm\\backend\\rete-algorithm\\src\\examples\\Social.clp",
    #                              True)
    # print(type(file_response))
    # print_response_node(file_response, 0)
