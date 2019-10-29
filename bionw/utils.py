import json


def read_fasta_file(file):
    return read_fasta(open(file, "r").read())


def read_fasta(data: str) -> str:
    lines = data.splitlines()[1:]
    if len(lines) < 1:
        raise ValueError("Input sequences should be in FASTA format")
    return "".join(lines)


class Config:
    def __init__(self, same, diff, gap, max_paths, max_sequence_length):
        self.same = same
        self.diff = diff
        self.gap = gap
        self.max_paths = max_paths
        self.max_sequence_length = max_sequence_length


def read_config_file(file: str) -> Config:
    config_content = open(file, "r").read()
    return read_config(config_content)


def read_config(config_content: str) -> Config:
    try:
        config_dict = json.loads(config_content)
        return Config(
            int(config_dict["SAME"]),
            int(config_dict["DIFF"]),
            int(config_dict["GAP_PENALTY"]),
            int(config_dict["MAX_NUMBER_PATHS"]),
            int(config_dict["MAX_SEQ_LENGTH"]),
        )
    except json.JSONDecodeError as e:
        raise ValueError("Error parsing config file") from e
    except KeyError as e:
        raise KeyError("Missing config parameter") from e
    except ValueError as e:
        raise ValueError("Incorrect type of parameter") from e
