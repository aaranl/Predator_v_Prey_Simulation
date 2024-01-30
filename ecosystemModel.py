from mesa import Model
from mesa.time import RandomActivation
from predator import Predator
from prey import Prey



class EcosystemModel(Model):
    """A model with predators and prey."""

    def __init__(self, num_predators, num_prey):
        self.num_predators = num_predators
        self.num_prey = num_prey
        self.schedule = RandomActivation(self)
        
        # Create predators
        for i in range(self.num_predators):
            predator = Predator(i, self)
            self.schedule.add(predator)
        
        # Create prey
        for i in range(self.num_prey):
            prey = Prey(i + self.num_predators, self)
            self.schedule.add(prey)

    def step(self):
        """Advance the model by one step."""
        self.schedule.step()

