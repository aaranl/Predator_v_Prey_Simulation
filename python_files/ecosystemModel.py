class EcosystemModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, num_predators, num_prey):
        self.num_predators = num_predators
        self.num_prey = num_prey
        # Create scheduler and assign it to the model
        self.schedule = mesa.time.RandomActivation(self)

        # Create agents
        for i in range(self.num_predators):
            predator = Predator(i, self)
            self.schedule.add(predator)
        
        for i in range(self.num_prey):
            prey = Prey(i + self.num_predators, self)
            self.schedule.add(prey)

    def step(self):
        """Advance the model by one step."""
        self.schedule.step()

