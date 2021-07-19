from cocu import lines, values


def test_number_of_values():
    nvalues = int(lines[9].split('**')[1])
    assert len(values) == nvalues, "Number of values should match"
