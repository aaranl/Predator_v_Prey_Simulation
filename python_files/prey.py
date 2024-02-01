class Prey(mesa.Agent):
    """ A prey agent """
    
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        # TODO: Add prey properties here
        self.is_prey = True
        self.life = 10
        

    def step(self):
        # TODO: Define prey behavior here
        if self.life > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent is not None and other_agent.is_prey:
                self.life += 1
                other_agent.life += 1
            else:
                self.life -= 1
                other_agent.life += 1
                