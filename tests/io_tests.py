import pytest
import bionw.utils as utils


def test_read_fasta():
    input = ">gi|186681228|ref|YP_001864424.1| phycoerythrobilin:ferredoxin oxidoreductase\nMARS"

    assert "MARS" == utils.read_fasta(input)


def test_read_fasta_multiline():
    input = ">gi|186681228|ref|YP_001864424.1| phycoerythrobilin:ferredoxin oxidoreductase\nMARS\nLONG"

    assert "MARSLONG" == utils.read_fasta(input)


def test_read_config():
    input = """
    {
        "SAME": 5,
        "DIFF": -5,
        "GAP_PENALTY": -2,
        "MAX_NUMBER_PATHS": 99,
        "MAX_SEQ_LENGTH": 9999
    }
    """

    config = utils.read_config(input)

    assert config.same == 5
    assert config.diff == -5
    assert config.gap == -2
    assert config.max_paths == 99
    assert config.max_sequence_length == 9999

def test_read_config_incorrect_format():
    input = """
    {
        "SAME": 5,
        "DIFF": -5,
        "GAP_PENALTY": -2,
        "ERROR": 99,/
        "MAX_SEQ_LENGTH": 9999
    }
    """

    with pytest.raises(ValueError):
        config = utils.read_config(input)

def test_read_config_incorrect_parameters():
    input = """
    {
        "SAME": 5,
        "DIFF": -5,
        "GAP_PENALTY": -2,
        "ERROR": 99,
        "MAX_SEQ_LENGTH": 9999
    }
    """

    with pytest.raises(KeyError):
        config = utils.read_config(input)

def test_read_config_incorrect_type():
    input = """
    {
        "SAME": 5,
        "DIFF": -5,
        "GAP_PENALTY": -2,
        "MAX_NUMBER_PATHS": 99,
        "MAX_SEQ_LENGTH": "x"
    }
    """

    with pytest.raises(ValueError):
        config = utils.read_config(input)
