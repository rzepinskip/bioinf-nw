# bionfnw

Implementation of the [Needleman-Wunsch algorithm](https://en.wikipedia.org/wiki/Needleman–Wunsch_algorithm) for bioinformatics course at the Warsaw University of Technology.

# Setup

The CLI can be installed using:

```
git clone www.github.com/rzepinskip/bioinf-nw
cd bioinf-nw
python -m venv .env
source .env/bin/activate
python setup.py install
```

Example usage:
```
python cli.py -a resources/seq1 -b resources/seq2 -c resources/config -o output
```

# Config

The algorithm can be tuned using configuration file:

```
{
    "SAME": 5,
    "DIFF": -5,
    "GAP_PENALTY": -2,
    "MAX_NUMBER_PATHS": 0,
    "MAX_SEQ_LENGTH": 999
}
```

`SAME` - value given when sequences match at some index
`DIFF` - value given when sequences differ at some index
`GAP_PENALTY` - value given when gap is inserted into one the sequences
`MAX_NUMBER_PATHS` - maximum number of alignments retrieved
`MAX_SEQ_LENGTH` - maximum length of input sequence

# Authors

`bioinfnw` was written by `Paweł Rzepiński <rzepinski.pawel@gmail.com>`_.
