import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random 


# -------------------------------------------------------------------------------------
# defining parameters

grid_width = 20
grid_height = 20

fish_stock = 1000
max_fish = 1000
min_fish = 200
regen_rate = 0.10

number_of_fishers = 20

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
        "behavior": random.randint(1, 9)}
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

def fish(): #Jeder Fischer fängt Fische. der behavior- WErt bestimmt die Fangmenge. (1 kooperativ, 9 egoistisch)
    global fish_stock
    
    total_catch = 0
    
    for fisher in fishers:
        total_catch += fisher["behavior"]
    
    print("Anzahl Fischer:", len(fishers))
    print("Max behavior:", max(f["behavior"] for f in fishers))
    print("Total catch:", total_catch)
        
    fish_stock -= total_catch
    if fish_stock < 0:
            fish_stock = 0

def adapt_behavior(): #Fischer passen ihr Verhalten an. Ohne Nachbar wird Fisher egoistisch. Mit Nachbarn: Der Fischer orientiert sich am stärksten ausgeprägtesten Verhalten in seiner Nachbarschaft. 
    for fisher in fishers:
        neighbors = get_neighbors(fisher)
        
        if len(neighbors) == 0:
            fisher["behavior"] += 1
        else:
            strongest_neighbor = neighbors[0]
            for neighbor in neighbors:
                if abs(neighbor["behavior"] - 5) > abs(strongest_neighbor["behavior"] - 5):
                    strongest_neighbor = neighbor
            if fisher["behavior"] < strongest_neighbor["behavior"]:
                fisher["behavior"] += 1
            elif fisher["behavior"] > strongest_neighbor["behavior"]:
                fisher["behavior"] -= 1
                
        if fisher["behavior"] < 1:
            fisher ["behavior"] = 1
            
        if fisher ["behavior"] > 9:
            fisher ["behavior"] = 9
    
def move_fishers(): #Jeder Fischer bewegt sich zufällig ein Feld weiter. (Moore-Nachbarschaft)
    for fisher in fishers:
        fisher["x"] += random.randint(-1, 1)
        fisher["y"] += random.randint(-1, 1)
        
        if fisher["x"] < 0:
            fisher["x"] = 0
        if fisher["x"] >= grid_width:
            fisher["x"] = grid_width - 1
        
        if fisher["y"] < 0:
            fisher["y"] = 0
        if fisher["y"] >= grid_height:
            fisher["y"] = grid_height - 1
            
def regenerate_fish(): #Fischbestand regeneriert sich. Pro Zeitschritt +10% (max 1000)
    global fish_stock
    
    fish_stock += fish_stock * regen_rate
    if fish_stock > max_fish:
        fish_stock = max_fish

def simulation_step(): #Führt einen kompletten Simulationsschritt aus: Fischer fischen, Verhalten wird angepasst, Fischer bewegen sich, Fische regenerieren sich.
    global current_step
    
    fish()
    adapt_behavior()
    move_fishers()
    regenerate_fish()
    
    current_step += 1
    

#------------------------------------------------------------------------------------
#Hilfsfunktionen für Simulationsanzeige

def get_colors(): #Gibt jedem Fischer eine Farbe je nach Verhalten. Grün = kooperativ, Gelb = mittel, Rot = Egoistisch
    colors = []
    for fisher in fishers:
        if fisher["behavior"] <=3:
            colors.append("green")
        elif fisher["behavior"] <= 6:
            colors.append("yellow")
        else: 
            colors.append("red")
    return colors
    
def get_fish_stock_color(): #Farbcode für den Fischbestand: Grün = Stabil, Orange = Bestand kritisch, Rot = Kipppunkt erreicht
     if fish_stock > 500:
         return "green"
     elif fish_stock > min_fish:
         return "orange"
     else:
         return "red"
def count_cooperative_fishers(): # Zählt die kooperativen Fischer 1-3
    return sum(1 for fisher in fishers if fisher["behavior"] <= 3)

def count_egoistic_fishers(): # Zählt die egoistischen Fischer 7-9
    return sum(1 for fisher in fishers if fisher["behavior"] >= 7)

#------------------------------------------------------------------------------------------
#Visualisierung mit matplotlib

fig, ax = plt.subplots(figsize=(7,7))

def update(frame): # Diese Funktion wird immer wieder aufgerufen, Dadurch entsteht die Animation. 
    global fish_stock, current_step
    
    ax.clear()
    
    if fish_stock > min_fish and current_step < time_steps:
       simulation_step()
       print("Schritt:", current_step, "fischbestand:", fish_stock)
    
    x_values = [fisher["x"] for fisher in fishers]
    y_values = [fisher["y"] for fisher in fishers]
    
    ax.set_facecolor("lightblue")
    
    ax.scatter(x_values, y_values, c=get_colors(), s=130, edgecolors="black")
    
    ax.set_xlim(-1, grid_width)
    ax.set_ylim(-1, grid_height)
    
    ax.set_xticks(range(grid_width))
    ax.set_yticks(range(grid_height))
    ax.grid(True)
    
    ax.set_title(f"Schritt: {current_step} | Fischbestand: {int(fish_stock)}")
    
animation = FuncAnimation(fig, update, frames=range(time_steps), interval=1000, repeat=False, cache_frame_data=False)
plt.show()
    
    
    
   