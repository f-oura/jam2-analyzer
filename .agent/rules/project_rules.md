# Project rules for jam2-analyzer

These rules are for the Antigravity agent to follow when working on this project.

## Environment Management
- ALWAYS run `module load gcc/1230` before any build or execution command if using a RedHat/CentOS-like environment (KEKCC).
- ALWAYS ensure `PYTHIA8` and `LD_LIBRARY_PATH` are derived from the logic in `setup.sh`.

## Repository Integrity
- DO NOT commit files inside `jam2-code/` or `deps/` directly to the main repository.
- Use `patches/jam2_compatibility.patch` as the source of truth for custom modifications to the submodule.
- Large data files (e.g., `*.dat`, `*.dat.gz`, `*.root`) MUST be ignored via `.gitignore`.
- Binary directories like `install/`, `bin/`, and `lib/` MUST NOT be committed.
