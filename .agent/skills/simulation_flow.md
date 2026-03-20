# Skill: Simulation Workflow

This skill describes the standard procedure for running simulations in `jam2-analyzer`.

## Goal
Running a new physical simulation using JAM2 and Pythia.

## Standard Procedure
1.  **Input Preparation**: Create or modify an input file in the `input/` directory (e.g., `input/my_setting.inp`).
2.  **Setup Environment**: Ensure the correct compiler and libraries are loaded:
    ```bash
    module load gcc/1230
    ./setup.sh
    ```
3.  **Execute Simulation**: Run the simulation using the `-f` flag for the input file:
    ```bash
    ./jam2-code/install/bin/jam -f input/my_setting.inp
    ```
4.  **Output Identification**: Common output files include `phase.dat.gz` and `ROOT` files if enabled in the analysis settings.
