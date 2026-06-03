import matplotlib.pyplot as plt
import numpy as np
import random 

#defining parameters

grid_width=20
grid_height=20

fish_stock=1000
max_fish = 1000
min_fish = 200

fisher=20

max_capacity_lake=1000
min_capacity_lake=200
regen_rate = 0.1

behave_factor_f=5 # 0 - 9 for fisher
behvave_factor_gr=0.5 # 0 - 1 for group

time_steps=1000

random.seed(42) # Fester/Gleicher Zufalls-Seed für Reproduzierbarkeit

# fishers 
