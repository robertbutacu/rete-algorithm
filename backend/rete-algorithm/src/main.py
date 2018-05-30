"E:\\Projects\\rete-algorithm\\backend\\rete-algorithm\\src\\examples\\Social.clp"
from src.services.ServerServices import build_network
from src.services.TransformerServices import get_text, print_network

if __name__ == "__main__":
    network = build_network(
        get_text("E:\\Projects\\rete-algorithm\\backend\\rete-algorithm\\src\\examples\\Sillogismi.clp"), False)
        #get_text("C:\\Users\\uanca\\Desktop\\pbr\\rete-algorithm\\backend\\rete-algorithm\\src\\examples\\MissionariCannibali.clp"),
    print(network[-1].to_dict())

    #file_response = build_network("E:\\Projects\\rete-algorithm\\backend\\rete-algorithm\\src\\examples\\general-truths.clp",
    #                              True)
   # print_network(file_response.states)
