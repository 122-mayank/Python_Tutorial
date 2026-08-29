"""
Suppose Project A needs:
numpy version X

while Project B needs:
numpy version Y

Installing everything globally can cause conflicts.
So we create:

Project A
   ↓
Virtual Environment A

Project B
   ↓
Virtual Environment B

Each project gets an isolated Python environment.

Typical command:
python -m venv .venv

Then activate the environment.
This is essential professional Python knowledge

"""