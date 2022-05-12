import re

from cocu import lines


def test_n_principles():
    idx = 0
    line = lines[idx]
    while not line.startswith("## Guiding principles"):
        idx += 1
        line = lines[idx]
    
    idx += 1
    line = lines[idx]
    n_principles = 0
    regex = re.compile(r"#### [0-9]+.")

    while not line.startswith("## "):
        if regex.search(line):
            n_principles += 1
        idx += 1
        line = lines[idx]

    assert (n_principles == 8), f"The number of principles must be 8, found: {n_principles}"