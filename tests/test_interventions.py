import pytest

from tacmi.interventions import apply_intervention
from tacmi.scm import Intervention
from tacmi.toy import mechanism_a


def test_binary_intervention():
    assert Intervention("z1", 0).value == 0
    assert Intervention("z1", 1).value == 1


def test_unknown_variable_is_rejected():
    model = mechanism_a()

    with pytest.raises(ValueError):
        apply_intervention(
            model,
            (0, 1),
            Intervention("does_not_exist", 1),
        )


def test_intervention_changes_downstream_output():
    model = mechanism_a()

    # Normal computation:
    #
    # x = (1, 0)
    # z1 = 1
    # z2 = 0
    # y = 1

    normal_output, normal_state = model.evaluate((1, 0))

    assert normal_output == 1
    assert normal_state["z1"] == 1

    # Force z1 to zero.
    response = apply_intervention(
        model,
        (1, 0),
        Intervention("z1", 0),
    )

    assert response.internal_state["z1"] == 0

    # y must be recomputed using the intervened z1.
    assert response.output == 0