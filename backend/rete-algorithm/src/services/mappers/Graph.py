class Graph:
    def __init__(self, network):
        self.__network = network
        self.__production_memory = network.production_memory
        self.__wm = network.working_memory
        self.__agenda = network.agenda
        network.recognize_act_cycle()

    @property
    def network(self):
        return self.__network

    @network.setter
    def network(self, value):
        self.__network = value

    @property
    def production_memory(self):
        return self.__production_memory

    @production_memory.setter
    def production_memory(self, value):
        self.__production_memory = value

    @property
    def wm(self):
        return self.__wm

    @wm.setter
    def wm(self, value):
        self.__wm = value

    @property
    def agenda(self):
        return self.__agenda

    @agenda.setter
    def agenda(self, value):
        self.__agenda = value
