from tacmi.toy import (
    all_inputs,
    mechanism_a,
    mechanism_b,
    mechanism_c,
    mechanism_d,
)


EXPECTED_XOR = {
    (0, 0): 0,
    (0, 1): 1,
    (1, 0): 1,
    (1, 1): 0,
}


def test_all_inputs_are_binary_pairs():
    assert all_inputs() == [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1),
    ]


def test_mechanism_a_computes_xor():
    model = mechanism_a()

    for x, expected in EXPECTED_XOR.items():
        output, _ = model.evaluate(x)
        assert output == expected


def test_mechanism_b_computes_xor():
    model = mechanism_b()

    for x, expected in EXPECTED_XOR.items():
        output, _ = model.evaluate(x)
        assert output == expected


def test_mechanism_c_computes_xor():
    model = mechanism_c()

    for x, expected in EXPECTED_XOR.items():
        output, _ = model.evaluate(x)
        assert output == expected


def test_mechanism_d_is_not_xor():
    model = mechanism_d()

    outputs = [
        model.evaluate(x)[0]
        for x in all_inputs()
    ]

    xor_outputs = list(EXPECTED_XOR.values())

    assert outputs != xor_outputs