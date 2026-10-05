from __future__ import annotations

from dataclasses import dataclass

from tacmi.scm import Intervention, StructuralCausalModel


@dataclass(frozen=True)
class CausalResponse:
    input_value: tuple[int, int]
    intervention: Intervention
    output: int
    internal_state: dict[str, int]


def apply_intervention(
    model: StructuralCausalModel,
    input_value: tuple[int, int],
    intervention: Intervention,
) -> CausalResponse:
    output, state = model.evaluate(
        input_value,
        intervention=intervention,
    )

    if intervention.variable not in state:
        raise ValueError(
            f"Variable '{intervention.variable}' "
            "is not present in the model."
        )

    return CausalResponse(
        input_value=input_value,
        intervention=intervention,
        output=output,
        internal_state=state,
    )