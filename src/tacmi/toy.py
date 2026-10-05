from __future__ import annotations

from itertools import product

from tacmi.scm import StructuralCausalModel


BitPair = tuple[int, int]


def mechanism_a() -> StructuralCausalModel:
    return StructuralCausalModel(
        equations={
            "z1": lambda s: s["x1"] * (1 - s["x2"]),
            "z2": lambda s: (1 - s["x1"]) * s["x2"],
            "y": lambda s: s["z1"] + s["z2"],
        },
        output_variable="y",
    )


def mechanism_b() -> StructuralCausalModel:
    return StructuralCausalModel(
        equations={
            "z1": lambda s: s["x1"] * (1 - s["x2"]),
            "z2": lambda s: (1 - s["x1"]) * s["x2"],
            "u1": lambda s: s["z1"] + s["z2"],
            "u2": lambda s: s["z1"] - s["z2"],
            "y": lambda s: s["u1"],
        },
        output_variable="y",
    )


def mechanism_c() -> StructuralCausalModel:
    return StructuralCausalModel(
        equations={
            "s": lambda state: state["x1"] + state["x2"],
            "p": lambda state: state["x1"] * state["x2"],
            "y": lambda state: state["s"] - 2 * state["p"],
        },
        output_variable="y",
    )


def mechanism_d() -> StructuralCausalModel:
    return StructuralCausalModel(
        equations={
            "y": lambda state: state["x1"],
        },
        output_variable="y",
    )


def all_inputs() -> list[BitPair]:
    return list(product((0, 1), repeat=2))