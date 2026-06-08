import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random 


# -------------------------------------------------------------------------------------
# defining parameters

grid_width = 20
grid_height = 20

fish_stock = 8000
max_fish = 8000
min_fish = 0
regen_rate = 0.10

number_of_fishers = 200

time_steps = 1000
current_step = 0   # timesteps of simulation starts at 0

random.seed(42) # same random seed for reproducibility

# -------------------------------------------------------------------------------

# fishers get their positions and behaviours

fishers = []
for i in range(number_of_fishers):
    fisher = {
        "x": random.randint(0, grid_width - 1),
        "y": random.randint(0, grid_height - 1),
        "behavior": random.randint(1, 1)} # all fishers are cooperative at the beginning (behavior 1)
    fishers.append(fisher)
    
# ----------------------------------------------------------------------------------

# modell-functions

def get_neighbors(fisher):
    """Returns a list of neighboring fishers in the Moore neighborhood (8 surrounding cells)."""
    neighbors = []
    for other in fishers:
        if other == fisher:
            continue
        dx = abs(fisher["x"] - other["x"]) # distance between fishers x coordinate
        dy = abs(fisher["y"] - other["y"]) # distance between fishers y coordinate
        if dx == 1 and dy == 1: # if the other fisher is in the Moore neighborhood (including diagonals)
            neighbors.append(other) # add the other fisher to the list of neighbors
    return neighbors

def fish(): 
    """Every fisher catches fish. The behaviour value determines the catch amount(1 cooperative, 9 egoistic)."""
    global fish_stock # global fish stock will change, because everybody can access them 
    
    total_catch = 0
    
    for fisher in fishers:
        total_catch += fisher["behavior"] # the catch amount is determined by the behavior value of the fisher(1-9)
    
    print("Total catch:", total_catch)
        
    fish_stock -= total_catch
    if fish_stock < 0:
            fish_stock = 0 # so it won't turn negative

def adapt_behavior():
    """Fishers adapt their behavior. Without neighbors, fishers become egoistic. With neighbors: the fisher aligns with the most pronounced behavior in their neighborhood."""
    for fisher in fishers:
        neighbors = get_neighbors(fisher)
        
        if len(neighbors) == 0:
            fisher["behavior"] += 1
        else:
            strongest_neighbor = neighbors[0]
            for neighbor in neighbors:
                if abs(neighbor["behavior"] - 5) > abs(strongest_neighbor["behavior"] - 5): # the strongest neighbor is the one with the most pronounced behavior (farthest from 5)
                    strongest_neighbor = neighbor
            if fisher["behavior"] < strongest_neighbor["behavior"]: 
                fisher["behavior"] += 1 
            elif fisher["behavior"] > strongest_neighbor["behavior"]: 
                fisher["behavior"] -= 1 # if the fisher is less egoistic than the strongest neighbor, it becomes more egoistic. If it is more egoistic, it becomes more cooperative. If they are the same, it stays the same.
                
        if fisher["behavior"] < 1:
            fisher ["behavior"] = 1
            
        if fisher ["behavior"] > 9:
            fisher ["behavior"] = 9
    
def move_fishers():
    """Every fisher moves randomly one field further. (Moore neighborhood)"""
    for fisher in fishers:
        fisher["x"] += random.randint(-1, 1) # move randomly in x direction (-1, 0, or 1)
        fisher["y"] += random.randint(-1, 1) # move randomly in y direction (-1, 0, or 1)
        
        if fisher["x"] < 0:
            fisher["x"] = 0
        if fisher["x"] >= grid_width:
            fisher["x"] = grid_width - 1 # so they won't move out of the grid
        
        if fisher["y"] < 0:
            fisher["y"] = 0
        if fisher["y"] >= grid_height:
            fisher["y"] = grid_height - 1 # same as for x coordinate
            
def regenerate_fish():
    """Fish stock regenerates. Per time step +10%"""
    global fish_stock
    
    fish_stock += fish_stock * regen_rate
    if fish_stock > max_fish:
        fish_stock = max_fish # so it won't exceed the maximum fish stock

def simulation_step(): 
    """Does a complete simulationstep: Fishers catches, Behaviour adapts, fishers move, fish regenerate"""
    global current_step
    
    fish()
    adapt_behavior()
    move_fishers()
    regenerate_fish()
    
    current_step += 1 # increase the current step by 1 after each simulation step, so we can keep track of how many steps have been simulated
    

# ------------------------------------------------------------------------------------
# helping functions for simulation (with the help of AI)

def get_colors():
    """ Returns a list of colors for the fishers based on their behavior. Green for cooperative (1-3), Yellow for medium (4-6), Red for egoistic (7-9)."""
    colors = []
    for fisher in fishers:
        if fisher["behavior"] <=3:
            colors.append("green")
        elif fisher["behavior"] <= 6:
            colors.append("yellow")
        else: 
            colors.append("red")
    return colors
    
def count_cooperative_fishers():
    """ Returns the number of cooperative fishers (behavior 1-3)."""
    return sum(1 for fisher in fishers if fisher["behavior"] <= 3) 

def count_egoistic_fishers():
    """ Returns the number of egoistic fishers (behavior 7-9)."""
    return sum(1 for fisher in fishers if fisher["behavior"] >= 7)

#------------------------------------------------------------------------------------------
#Visualisations with matplotlib (with the help of AI)

fig, ax = plt.subplots(figsize=(7,7))

def update(frame):
    """ Updates the plot for each frame of the animation. It clears the plot, runs a simulation step, and then plots the fishers with colors based on their behavior. It also updates the title with the current step and fish stock."""
    global fish_stock, current_step
    
    ax.clear()
    
    if fish_stock > min_fish and current_step < time_steps:
       simulation_step()
       print("timestep:", current_step, "fishstock:", fish_stock)
    
    x_values = [fisher["x"] for fisher in fishers]
    y_values = [fisher["y"] for fisher in fishers]
    
    ax.set_facecolor("lightblue")
    
    ax.scatter(x_values, y_values, c=get_colors(), s=130, edgecolors="black")
    
    ax.set_xlim(-1, grid_width)
    ax.set_ylim(-1, grid_height)
    
    ax.set_xticks(range(grid_width)) 
    ax.set_yticks(range(grid_height))
    ax.grid(True) # add grid lines to the plot for better visibility of the fishers positions
    
    ax.set_title(f"timestep: {current_step} | fishstock: {int(fish_stock)}") # update the title with the current step and fish stock, so we can see how they change over time
    
animation = FuncAnimation(fig, update, frames=range(time_steps), interval=1000, repeat=False, cache_frame_data=False)
plt.show()
    
    
    
   