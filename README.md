# Running the Simulation

Requirements:
- Python 3.x
- uv

Start the simulation with:

```bash
uv run main_szenario.py
```

The simulation opens an animated visualization of both scenarios and generates a comparison of the fish stock development.

The following model parameters can be modified directly in the source code:

- timesteps = 200 (original setting)
- start_fish = 5000 (original setting)
- max_fish = 5000 (original setting)
- min_fish = 0 (original setting)
- regen_rate = 0.0366 (3.66 %, original setting)