import random
import mesa


class PreyAgent(mesa.Agent):
    """
    Prey Agent
    """

    def __init__(self, pos, model, energy):
        """
        Create a new Prey agent.

        Args:
           unique_id: Unique identifier for the agent.
           x, y: Agent initial location.
           agent_type: Indicator for the agent's type (minority=1, majority=0)
        """

        # TODO: Add prey properties here
        super().__init__(pos, model)
        self.pos = pos
        self.energy = energy

    def step(self):

        # TODO: Define predator behavior here
        pass


class PredatorAgent(mesa.Agent):
    """
    Predator Agent
    """

    def __init__(self, pos, model, energy):
        """
        Create a new Predator agent.

        Args:
           unique_id: Unique identifier for the agent.
           x, y: Agent initial location.
           agent_type: Indicator for the agent's type (minority=1, majority=0)
        """

        # TODO: Add predator properties here
        super().__init__(pos, model)
        self.pos = pos
        self.energy = energy

    def step(self):
        # TODO: Define predator behavior here
        pass

class Environment(mesa.Model):
    """
    Model class for the Schelling segregation model.
    """

    def random_empty_cell(self):
        """
        Find a random empty cell in the grid.
        """
        empty_cells = [(coords[0], coords[1]) for coords, agent in self.grid.coord_iter() if agent is None]
        return random.choice(empty_cells) if empty_cells else None

    def __init__(self, width=20, height=20):
        super().__init__()
        self.grid = mesa.space.SingleGrid(width, height, torus=True)
        self.schedule = mesa.time.RandomActivation(self)

        # Create predators
        for _ in range(50):  # Number of predators
            empty_cell = self.random_empty_cell()
            if empty_cell is not None:
                x, y = self.grid.find_empty()
                energy = 20
                predator = PredatorAgent((x, y), self, energy)
                self.grid.place_agent(predator, (x, y))
                self.schedule.add(predator)
            

        # Create prey
        for _ in range(10):  # Number of prey
            empty_cell = self.random_empty_cell()
            if empty_cell is not None:
                x, y = empty_cell
                energy = 10
                prey = PreyAgent((x, y), self, energy)
                self.grid.place_agent(prey, (x, y))
                self.schedule.add(prey)

        self.running = True


    def step(self):
        """
        Run one step of the model. 
        """
        self.schedule.step()