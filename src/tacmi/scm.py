from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


Input = tuple[int, int]
Equation = Callable[[dict[str, int]], int]


@dataclass(frozen=True)
class Intervention:
    variable: str
    value: int


@dataclass
class StructuralCausalModel:
    """
    A tiny deterministic structural causal model.

    Variables are evaluated in topological order.
    An intervention replaces the structural equation of one variable.
    """

    equations: dict[str, Equation]
    output_variable: str

    def evaluate(
        self,
        inputs: Input,
        intervention: Intervention | None = None,
    ) -> tuple[int, dict[str, int]]:
        state: dict[str, int] = {
            "x1": inputs[0],
            "x2": inputs[1],
        }

        for variable, equation in self.equations.items():
            if intervention is not None and variable == intervention.variable:
                state[variable] = intervention.value
            else:
                state[variable] = equation(state)

        return state[self.output_variable], state