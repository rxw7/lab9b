import random

class Agent:
    def __init__(self, location=None):
        self.location = location

    def move(self, vacant_spots):
        self.location = random.choice(vacant_spots)

class World:
    def __init__(self, grid_size, num_agents):
        self.grid_size = grid_size
        self.grid = [[None for _ in range(grid_size)] for _ in range(grid_size)]
        self.agents = [Agent() for _ in range(num_agents)]
        self.populate_world()

    def populate_world(self):
        for agent in self.agents:
            while True:
                x, y = random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)
                if not self.grid[x][y]:
                    self.grid[x][y] = agent
                    agent.location = (x, y)
                    break

    def find_vacant(self):
        return [(x, y) for x in range(self.grid_size) for y in range(self.grid_size) if not self.grid[x][y]]

    def run_simulation(self, num_steps):
        for _ in range(num_steps):
            for agent in self.agents:

                vacant_spots = self.find_vacant()
                if vacant_spots:
 
                    x, y = agent.location
                    self.grid[x][y] = None
                    agent.move(vacant_spots)
                    new_x, new_y = agent.location
                    self.grid[new_x][new_y] = agent

if __name__ == "__main__":
    grid_size = 5  
    num_agents = 5  
    num_steps = 10  

    world = World(grid_size, num_agents)
    world.run_simulation(num_steps)
