# PyXRD – Claude Instructions

## Project Overview
PyXRD is a Python application for X-ray diffraction analysis of disordered layered minerals.
All source lives under `data/lib/python3.8/site-packages/pyxrd/` (bundled install, no separate src root).

## Repository
- GitHub: KazukiNoSuzaku/PyXRD
- Main branch: `main`
- Working branch: `V.2`

## Key Decisions
- **Pyro4 server is disabled.** `pyxrd/data/settings.py` uses only `DummyAsyncServerProvider`.
  Do not re-add `Pyro4AsyncServerProvider` unless explicitly asked.

## Watch Out For
- A linter may silently revert file edits. Always run `git diff` to confirm a change stuck before committing.
- The `data/lib/.../` path contains both `.py` source files and `.pyc` compiled files — edit only the `.py` files.
- `__pycache__` `.pyc` files show as modified in `git status` constantly — ignore them, do not stage or commit them.
