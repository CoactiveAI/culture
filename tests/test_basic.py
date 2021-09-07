from cocu import lines, values


def test_number_of_values():
    # FIXME: Use regex or something more robust
    nvalues = int(lines[10].split('**')[1])
    assert len(values) == nvalues, "Number of values should match"
