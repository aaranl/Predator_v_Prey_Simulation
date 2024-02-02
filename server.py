import mesa
from models import Environment, PredatorAgent, PreyAgent



def environment_draw(agent):
    """
    Portrayal Method for canvas
    """
    if isinstance(agent, PredatorAgent):
        portrayal = {"Shape": "circle", "Color": "red", "r": 0.5}
    elif isinstance(agent, PreyAgent):
        portrayal = {"Shape": "circle", "Color": "green", "r": 0.5}
    return portrayal



canvas_element = mesa.visualization.CanvasGrid(environment_draw, 20, 20, 500, 500)

model_params = {
    "height": 20,
    "width": 20,
}

server = mesa.visualization.ModularServer(
    Environment,
    [canvas_element],
    "Pred v Prey",
    model_params,
)