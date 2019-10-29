import numpy
import warnings
from typing import List, Any, Tuple, Dict
from .utils import Config

class NWAlgo:
    def __init__(self, config: Config):
        self._config = config

    def compute_cost_matrix(self, first_seq: str, second_seq: str) -> Any:
        pass

    def get_all_alignments(self, first_seq: str, second_seq: str, cost_matrix: Any):
        pass

    def _retrieve_previous_nodes(self, first_seq: str, second_seq: str, cost_matrix: Any):
        pass

    def _find_all_paths(
        self, 
        graph: Dict[Tuple[int, int], List[Tuple[int, int]]],
        start: Tuple[int, int],
        end: Tuple[int, int],
        path: List[Tuple[int, int]]
    ) -> List[List[Tuple[int, int]]]:
        pass