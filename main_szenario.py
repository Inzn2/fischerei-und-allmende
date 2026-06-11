import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# -------------------------------------------------------------------------------------
# Parameter

grid_width = 20
grid_height = 20

start_fish = 5000
max_fish = 5000
min_fish = 0
regen_rate = 0.0366  

number_of_fishers = 30

time_steps = 200

# -------------------------------------------------------------------------------------
# A class that simulates a single lake.
# The "rules" switch determines whether there are rules at the lake or not.
# This allows us to run two lakes with the exact same start against each other.

class Simulation:
    def __init__(self, rules, seed=42):
        self.rules = rules                  # True = with rules, False = without rules
        self.fish_stock = start_fish
        self.current_step = 0
        self.rng = random.Random(seed)      # own random generator -> reproducible.
        # Both simulations get the same seed -> same starting positions AND same
        # movements. Only the rules differ -> fair comparison.

        self.fishers = []
        for i in range(number_of_fishers):
            fisher = {
                "x": self.rng.randint(0, grid_width - 1),
                "y": self.rng.randint(0, grid_height - 1),
                "behavior": 1}              # all start cooperative (behavior 1)
            self.fishers.append(fisher)

        self.history = [self.fish_stock]    # fish stock per time step (for the final plot)
        self.total_caught = 0               # total fish caught
        self.catch_per_step = []            # fish caught per time step

    def get_neighbors(self, fisher):
        """Neighbors in the Moore neighborhood (the 8 surrounding cells)."""
        neighbors = []
        for other in self.fishers:
            if other is fisher:
                continue
            dx = abs(fisher["x"] - other["x"])
            dy = abs(fisher["y"] - other["y"])
            if dx <= 1 and dy <= 1:         # all 8 neighboring cells (previously only diagonals!)
                neighbors.append(other)
        return neighbors

    def fish(self):
        """Each fisher catches fish. behavior determines the catch amount (1 cooperative ... 9 egoistic)."""
        total_catch = 0
        for fisher in self.fishers:
            total_catch += fisher["behavior"]
        actual_catch = min(total_catch, self.fish_stock)   # cannot catch more than is available
        self.fish_stock -= actual_catch
        self.total_caught += actual_catch                  # running total over all steps
        self.catch_per_step.append(actual_catch)           # catch in this step

    def adapt_behavior(self):
        """This is where the whole difference between the two scenarios lies."""
        for fisher in self.fishers:
            neighbors = self.get_neighbors(fisher)

            if self.rules:
                # WITH rules: if you meet others -> you take care and fish less.
                # If you are alone -> the temptation to fish more increases a bit.
                if len(neighbors) > 0:
                    fisher["behavior"] -= 1
                else:
                    fisher["behavior"] += 1
            else:
                # WITHOUT rules: everyone just fishes more and more.
                fisher["behavior"] += 1

            # enforce bounds
            if fisher["behavior"] < 1:
                fisher["behavior"] = 1
            if fisher["behavior"] > 9:
                fisher["behavior"] = 9

    def move_fishers(self):
        """Each fisher moves randomly one field further, never onto an occupied cell."""
        for fisher in self.fishers:
            occupied = {(f["x"], f["y"]) for f in self.fishers if f is not fisher}

            new_x = fisher["x"] + self.rng.randint(-1, 1)
            new_y = fisher["y"] + self.rng.randint(-1, 1)

            if new_x < 0:
                new_x = 0
            if new_x >= grid_width:
                new_x = grid_width - 1
            if new_y < 0:
                new_y = 0
            if new_y >= grid_height:
                new_y = grid_height - 1

            if (new_x, new_y) not in occupied:
                fisher["x"] = new_x
                fisher["y"] = new_y

    def regenerate_fish(self):
        """Fish stock grows by +10% each time step."""
        self.fish_stock += self.fish_stock * regen_rate
        if self.fish_stock > max_fish:
            self.fish_stock = max_fish

    def step(self):
        """A complete simulation step: catch, adapt, move, regenerate."""
        self.fish()
        self.adapt_behavior()
        self.move_fishers()
        self.regenerate_fish()
        self.current_step += 1
        self.history.append(self.fish_stock)

    # ---- helper functions for visualization ----
    def get_colors(self):
        """Green = cooperative (1-3), yellow = medium (4-6), red = egoistic (7-9)."""
        colors = []
        for fisher in self.fishers:
            if fisher["behavior"] <= 3:
                colors.append("green")
            elif fisher["behavior"] <= 6:
                colors.append("yellow")
            else:
                colors.append("red")
        return colors

    def count_cooperative_fishers(self):
        return sum(1 for fisher in self.fishers if fisher["behavior"] <= 3)

    def count_egoistic_fishers(self):
        return sum(1 for fisher in self.fishers if fisher["behavior"] >= 7)


# -------------------------------------------------------------------------------------
# Two simulations: left without rules, right with rules (same seed -> fair comparison)

sim_no_rules = Simulation(rules=False)
sim_rules = Simulation(rules=True)


# -------------------------------------------------------------------------------------
# Animation: both lakes side by side

def draw_sim(ax, sim, title_prefix):
    """Draws a lake in the given axis."""
    ax.clear()
    ax.set_facecolor("lightblue")

    x_values = [fisher["x"] for fisher in sim.fishers]
    y_values = [fisher["y"] for fisher in sim.fishers]
    ax.scatter(x_values, y_values, c=sim.get_colors(), s=80, edgecolors="black")

    ax.set_xlim(-1, grid_width)
    ax.set_ylim(-1, grid_height)
    ax.set_xticks(range(0, grid_width, 2))
    ax.set_yticks(range(0, grid_height, 2))
    ax.grid(True)
    ax.set_title(f"{title_prefix}\nZeitschritt: {sim.current_step} | Fischbestand: {int(sim.fish_stock)}")


def update(frame):
    """Advances both lakes by one step and redraws them."""
    if sim_no_rules.current_step < time_steps:
        sim_no_rules.step()
    if sim_rules.current_step < time_steps:
        sim_rules.step()

    draw_sim(ax1, sim_no_rules, "OHNE Regeln (freies Fischen)")
    draw_sim(ax2, sim_rules, "MIT Regeln (Ruecksicht)")


if __name__ == "__main__":
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6.5))

    animation = FuncAnimation(fig, update, frames=range(time_steps),
                              interval=60, repeat=False, cache_frame_data=False)
    plt.tight_layout()
    plt.show()   # close the window -> then the comparison plot appears

    # ---------------------------------------------------------------------------------
    # Output: fish caught after 100 time steps (for both lakes)

    caught_100_no_rules = sum(sim_no_rules.catch_per_step[:100])
    caught_100_rules = sum(sim_rules.catch_per_step[:100])

    print("------------------------------------------------------------")
    print("Gefischte Fische nach 100 Zeitschritten:")
    print(f"  OHNE Regeln: {int(caught_100_no_rules)} Fische")
    print(f"  MIT  Regeln: {int(caught_100_rules)} Fische")
    print("------------------------------------------------------------")

    # ---------------------------------------------------------------------------------
    # Final plot: fish stock development in both scenarios

    plt.figure(figsize=(10, 6))
    plt.plot(sim_no_rules.history, color="red", label="OHNE Regeln")
    plt.plot(sim_rules.history, color="green", label="MIT Regeln")
    plt.axhline(0, color="gray", linewidth=0.8)
    plt.axvline(100, color="black", linestyle="--", linewidth=0.8)   # mark at 100 steps
    plt.text(150, plt.ylim()[1] * 0.97,
             f"  nach 100 Schritten gefischt:\n  OHNE Regeln: {int(caught_100_no_rules)}\n  MIT Regeln: {int(caught_100_rules)}",
             va="top", fontsize=9)
    plt.xlabel("Zeitschritt")
    plt.ylabel("Fischbestand")
    plt.title("Entwicklung des Fischbestands: mit vs. ohne Regeln")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()