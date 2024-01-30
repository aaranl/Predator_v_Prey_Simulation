from predator import Predator
from python_files.prey import Prey
from python_files.ecosystemModel import EcosystemModel
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.UserParam import UserSettableParameter


def agent_portrayal(agent):
    size = 10 
    color = "tab:red"
    if type(agent) is Predator:
        portrayal = {

                     "Filled": "true",
                     "Layer": 0,
                     "r": 0.5}
    elif type(agent) is Prey:
        portrayal = {"Shape": "circle",
                     "Color": "green",
                     "Filled": "true",
                     "Layer": 1,
                     "r": 0.5}
    return portrayal


grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)

server = ModularServer(EcosystemModel,
                       [grid],
                       "Ecosystem Model",
                       {"num_predators": UserSettableParameter('slider', 'Number of Predators', 5, 1, 10),
                        "num_prey": UserSettableParameter('slider', 'Number of Prey', 15, 1, 30)})
server.port = 8521  # You can change this if the port is in use
server.launch()